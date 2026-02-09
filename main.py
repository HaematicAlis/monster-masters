from card import Card
from files import import_cards
from deck import build_deck_from_list

CARD_DATA_PATH = "data/cards.csv"

def main():
    card_dict = import_cards(CARD_DATA_PATH)

main()
