from engine.card import Card
from engine.deck import Deck, build_deck_from_list

def import_cards(filepath):
    card_dict = {}

    with open(filepath) as cards_csv:
        cards = cards_csv.readlines()
        for card in cards[1:]:
            card_fields = card.split(",")
            set_id = card_fields[0]
            name = card_fields[1].strip()
            card_dict[set_id] = { "set_id": set_id, "name": name }

    return card_dict

def import_decklist(filepath):
    with open(filepath) as deckfile:
        lines = deckfile.readlines()
        name = lines[0]
        decklist = lines[1:]
        return build_deck_from_list(name, decklist)
