from engine.card import Card
from engine.files import import_cards
from engine.deck import build_deck_from_list
from engine.db import init_card_dict

CARD_DATA_PATH = "../data/cards.csv"

def main():
    card_dict = import_cards(CARD_DATA_PATH)
    init_card_dict(card_dict)

main()
