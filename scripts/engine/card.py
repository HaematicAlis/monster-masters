class Card:
    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name

    def __str__(self):
        return f"{self.card_id}: {self.name}"
