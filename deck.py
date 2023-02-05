from card import Card
import datetime
import json
from json.decoder import JSONDecodeError
import numpy as np

class Deck:
    def __init__(self):
        self.cards = []

    def add(self, term, definition):
        c = Card(term, definition, datetime.datetime.now(), 1)
        self.cards.append(c)

    def remove(self, term):
        # make new list w/out flashcard
        self.cards = [x for x in self.cards if x.term != term]

    def display_deck(self):
        for card in self.cards:
            x = str(card.next_review)
            print(x.split(" ", 1)[0] + ' ' + card.term + ': ' + card.definition + '\n')

        change_term = input('If you would like to edit a card, enter the cards term\n')
        #if any(card.term == term for card in self.cards):
        card = next((card for card in self.cards if card.term == change_term), False)
        if card:
            new_def = input('type the new definition for this card\n')
            card.definition = new_def





    def study(self, amount):
        # get all cards that need to be reviewed today
        cards = [x for x in self.cards if x.next_review < datetime.datetime.now()]
        try:
            amount = int(amount)
        except ValueError:
            amount = len(cards)

        remaining = len(cards) - amount
        while amount > 0:
            # only want to pull random cards from list of cards for today
            idx = np.random.randint(0, len(self.cards))
            card = self.cards[idx]
            if card.next_review < datetime.datetime.now():
                print(amount)
                print('--------------------------------------------------------------------------------')
                print('\n\n' + card.term + '\n\n')
                print('--------------------------------------------------------------------------------')
                input('press enter for answer\n')
                print('--------------------------------------------------------------------------------')
                print('\n\n' + card.definition + '\n\n')
                print('--------------------------------------------------------------------------------')
                user_answer = input('type c for correct, n for incorrect\n')
                if user_answer == 'c':
                    amount -= 1
                    # need to update review time in self.cards and deck of currently being studied
                    card.update_review_time(True)
                else:
                    card.update_review_time(False)
                leave = input('do you want to exit, e = exit')
                if leave == 'e':
                    break

        print('Number of cards remaining to be studied today: ' + str(remaining))

    def study_all(self):
        for card in self.cards:
            print('--------------------------------------------------------------------------------')
            print('\n\n' + card.term + '\n\n')
            print('--------------------------------------------------------------------------------')
            input('press enter for answer\n')
            print('--------------------------------------------------------------------------------')
            print('\n\n' + card.definition + '\n\n')
            print('--------------------------------------------------------------------------------')
            user_answer = input('type c for correct, n for not correct\n')
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
            try:
                data = json.load(infile)
                self.cards = [Card(card['term'], card['definition'], datetime.datetime.fromisoformat(card['next_review']), card['lastTime']) for card in data]
            except JSONDecodeError:
                self.cards = []

