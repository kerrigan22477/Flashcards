import datetime

class Card:
    def __init__(self, term, definition, next_review):
        self.term = term
        self.definition = definition
        self.next_review = next_review
        self.lastTime = 1

    def update_definition(self, new):
        self.definition = new

    def update_review_time(self, correct):
        if correct:
            self.next_review = datetime.datetime.now() + datetime.timedelta(days=self.lastTime*2)
            self.lastTime = self.lastTime*2
        else:
            #self.next_review = datetime.datetime.now() + datetime.timedelta(days=1)
            self.lastTime = 1

    def to_dict(self):
        return {
            'term': self.term,
            'definition': self.definition,
            'next_review': self.next_review.isoformat()
        }


