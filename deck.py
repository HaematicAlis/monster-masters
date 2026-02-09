from utility import search_card_by_id

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        if self.cards == []:
            return "! Deck is empty."
        card_list = ""
        for card in self.cards:
            card_list += f"{card}\n"
        return card_list

def build_deck_from_list(card_dict, decklist):
    cards_in_deck = []
    for card_id in decklist:
        card_to_add = search_card_by_id(card_dict, card_id)
        if card_to_add == None:
            continue
        cards_in_deck.append(card_to_add)
    return Deck(cards_in_deck)
