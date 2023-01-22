import datetime

class Card:
    def __init__(self, term, definition):
        self.term = ''
        self.definition = ''
        self.next_review = datetime.datetime.now()
        self.lastTime = 1

    def getTerm(self):
        return self.term

    def getDefinition(self):
        return self.definition

    def update_review_time(self, correct):
        if correct:
            self.next_review = datetime.datetime.now() + datetime.timedelta(days=self.lastTime+3)
            self.lastTime = self.lastTime + 3
        else:
            self.next_review = datetime.datetime.now() + datetime.timedelta(days=1)
            self.lastTime = 1

    def to_dict(self):
        return {
            'term': self.term,
            'definition': self.definition,
            'next_review': self.next_review.isoformat()
        }


