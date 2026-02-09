from card import Card

def import_cards(filepath):
    all_cards = []

    with open(filepath) as cards_csv:
        cards = cards_csv.readlines()
        for card in cards[1:]:
            card_fields = card.split(",")
            card_id = card_fields[0]
            name = card_fields[1].strip()
            all_cards.append(Card(card_id, name))

    return all_cards
