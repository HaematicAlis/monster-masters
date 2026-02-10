from engine.card import Card
from engine.files import import_cards
from engine.deck import build_deck_from_list
from engine.search import search_card_by_id
from engine.db import init_card_dict

card_dict = import_cards("../data/cards.csv")
init_card_dict(card_dict)

def test_build():
    test_cases = [
        ("testdeck", ["SP01", "SP02"], "[testdeck]\nSP01: Monster Master\nSP02: Pickle Fly\n"),
        ("testdeck", ["SP03", "SP03"], "[testdeck]\nSP03: Star Complete\nSP03: Star Complete\n"),
        ("testdeck", ["SP01", "SP04"], "[testdeck]\nSP01: Monster Master\n"),
        ("testdeck", ["SP02"], "[testdeck]\nSP02: Pickle Fly\n"),
        ("testdeck", ["SP05"], "! Deck is empty."),
        ("testdeck", [], "! Deck is empty.")
    ]

    for name, decklist, expected_output in test_cases:
        deck = build_deck_from_list(name, decklist)
        print(f"input: {name}, {decklist}")
        print("expected:")
        print(expected_output)
        print("actual:")
        print(deck)
        if (str(deck) == expected_output):
            print("===== PASS =====")
        else:
            print("===== FAIL =====")
 
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

