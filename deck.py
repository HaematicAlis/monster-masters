from utility import search_card_by_id

class Deck:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def __str__(self):
        if self.cards == []:
            return "! Deck is empty."
        card_list = f"[{self.name}]\n"
        for card in self.cards:
            card_list += f"{card}\n"
        return card_list

def build_deck_from_list(name, decklist):
    cards_in_deck = []
    for card_id in decklist:
        card_to_add = search_card_by_id(card_id)
        if card_to_add == None:
            continue
        cards_in_deck.append(card_to_add)
    return Deck(name, cards_in_deck)
