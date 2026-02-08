from card import Card
def main():
    sp_cards = []

    with open("cards/sp.csv") as sp:
        cards = sp.readlines()
        for card in cards[1:]:
            card_fields = card.split(",")
            card_id = card_fields[0]
            name = card_fields[1]
            sp_cards.append(Card(card_id, name))
        
        for card in sp_cards:
            print(card)

main()
