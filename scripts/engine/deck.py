from engine.search import search_card_by_id
from engine.card import Card
from engine.zone import Zone

class Deck:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def __str__(self):
        if self.cards == []:
            return "! Deck is empty."
        card_list = f"[Deck: {self.name}] ({len(self.cards)})"
        for card in self.cards:
            card_list += f"\n{card}"
        return card_list

    def build(self, deck_zone):
        for card_id in self.cards:
            card_info = search_card_by_id(card_id)
            if card_info == None:
                continue
            deck_zone.add(card_info)
