from engine.card import Card
from engine.deck import Deck, build_deck_from_list

def import_cards(filepath):
    card_dict = {}

    with open(filepath) as cards_csv:
        cards = cards_csv.readlines()
        for card in cards[1:]:
            card_fields = card.split(",")
            set_id = card_fields[0]
            name = card_fields[1]
            level = card_fields[2]
            typeline = card_fields[3]
            abilities = card_fields[4]
            rarity = card_fields[5]
            color = card_fields[6]
            cost = card_fields[7].strip()

            abilities_arr = abilities.split(";")
            cost_arr = cost.split(";")

            card_dict[set_id] = {
                "set_id": set_id,
                "name": name,
                "level": int(level),
                "typeline": typeline,
                "abilities": abilities_arr,
                "rarity": rarity,
                "color": color,
                "cost": cost_arr
            }

    return card_dict

def import_decklist(filepath):
    with open(filepath) as deckfile:
        lines = deckfile.readlines()
        name = lines[0]
        decklist = lines[1:]
        return build_deck_from_list(name, decklist)
