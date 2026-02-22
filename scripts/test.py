from engine.card import Card
from engine.files import import_cards, import_decklist
from engine.deck import build_deck_from_list
from engine.search import search_card_by_id
from engine.db import init_card_dict
from engine.zone import Zone

card_dict = import_cards("data/cards.csv")
init_card_dict(card_dict)

def test_build():
    deck = import_decklist("decks/test.deck", 1)    
    print(deck)

def test_zones():
    deck_zone = Zone("deck", 1)
    hand_zone = Zone("hand", 1)
    hand_zone.reveal_to_player(1)
    print("===== ADD =====")
    deck_zone.add(card_dict["sp01"])
    deck_zone.add(card_dict["sp02"])
    deck_zone.add(card_dict["sp03"])
    deck_zone.add(card_dict["sp02"])
    print(deck_zone)
    print("===== REMOVE BY INDEX =====")
    deck_zone.remove(0)
    print(deck_zone)
    print("===== REMOVE NOT EXIST =====")
    deck_zone.remove(7)
    print(deck_zone)
    print("===== CHANGE ZONES =====")
    deck_zone.move(2, hand_zone)
    print(deck_zone)
    print(hand_zone)
    print("===== CHANGE FROM NOT EXIST =====")
    deck_zone.move(5, hand_zone)
    print(deck_zone)
    print(hand_zone)
    print("===== CHANGE TO OWN ZONE =====")
    deck_zone.move(0, deck_zone, 2)
    print(deck_zone)
    print(hand_zone)
    print("===== CHANGE CREATES EMPTY =====")
    hand_zone.move(0, deck_zone, 1)
    print(deck_zone)
    print(hand_zone)
 
def test_search():
    test_cases = [
        ("SP01", "Monster Master"),
        ("SP02", "Pickle Fly"),
        ("SP03", "Star Complete"),
        ("SP04", None)
    ]

    for card_id, expected_output in test_cases:
        card = search_card_by_id(card_id)
        if card == None:
            name = None
        else:
            name = card.name
        print(f"input: {card_id}")
        print(f"expected: {expected_output}")
        print(f"actual: {name}")
        if (name == expected_output):
            print("===== PASS =====")
        else:
            print("===== FAIL =====")

test_build()
#test_search()
#test_zones()
