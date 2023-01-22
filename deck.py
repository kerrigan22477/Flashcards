from card import Card
import datetime
import json

class Deck:
    def __init__(self):
        self.cards = []

    def add(self, term, definition):
        c = Card(term, definition)
        self.cards.append(c)

    def study(self):
        for card in self.cards:
            if datetime.datetime.now() < card.next_review():
                print(card.getTerm())
                input('press enter for answer')
                print(card.getDefinition())
                user_answer = input('type c for correct, n for not correct')
                if user_answer == 'c':
                    card.update_review_time(True)
                else:
                    card.update_review_time(False)

    def save(self, filename):
        data = [card.to_dict() for card in self.cards]
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    def load(self, filename):
        with open(filename, 'r') as infile:
            data = json.load(infile)
        self.cards = [Card(card['term'], card['definition'], datetime.datetime.fromisoformat(card['next_review'])) for card in data]

