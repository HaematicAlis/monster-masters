from card import Card

def import_set(filepath):
    set_cards = []

    with open(filepath) as set_list:
        cards = set_list.readlines()
        for card in cards[1:]:
            card_fields = card.split(",")
            card_id = card_fields[0]
            name = card_fields[1]
            set_cards.append(Card(card_id, name))

    return set_cards
