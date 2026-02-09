from card import Card
from files import import_set

def main():
    sp_cards = import_set("cards/sp.csv")

    for card in sp_cards:
        print(card)

main()
