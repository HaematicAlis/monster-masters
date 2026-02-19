largest_uid = 0
created_cards = {}

class Card:
    def __init__(self, set_id, name):
        global largest_uid
        largest_uid += 1
        self.uid = largest_uid
        self.set_id = set_id
        self.name = name
        created_cards[self.uid] = self

    def __str__(self):
        return f"UID{self.uid}: {self.name}"
