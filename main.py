from card import Card
from files import import_cards

def main():
    all_cards = import_cards("data/cards.csv")

    for card in all_cards:
        print(card)

main()
