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
            card_list += f"\n{card.name}"
        return card_list

def build_deck_from_list(name, decklist, pid):
    deck_zone = Zone(f"deck_{pid}", pid)
    cards_in_deck = []
    for card_id in decklist:
        card_info = search_card_by_id(card_id)
        if card_info == None:
            continue
        card_to_add = Card(card_info, deck_zone)
        cards_in_deck.append(card_to_add)
    return Deck(name, cards_in_deck)
