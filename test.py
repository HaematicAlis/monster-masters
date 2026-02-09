from card import Card
from files import import_cards
from deck import build_deck_from_list
from utility import search_card_by_id

card_dict = import_cards("data/cards.csv")

def test_build():
    test_cases = [
        (["SP01", "SP02"], "Name: Monster Master\nName: Pickle Fly\n"),
        (["SP03", "SP03"], "Name: Star Complete\nName: Star Complete\n"),
        (["SP01", "SP04"], "Name: Monster Master\n"),
        (["SP02"], "Name: Pickle Fly\n"),
        (["SP05"], "! Deck is empty."),
        ([], "! Deck is empty.")
    ]

    for case_input, expected_output in test_cases:
        deck = build_deck_from_list(card_dict, case_input)
        print(f"input: {case_input}")
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

    for case_input, expected_output in test_cases:
        card = search_card_by_id(card_dict, case_input)
        if card == None:
            name = None
        else:
            name = card.name
        print(f"input: {case_input}")
        print(f"expected: {expected_output}")
        print(f"actual: {name}")
        if (name == expected_output):
            print("===== PASS =====")
        else:
            print("===== FAIL =====")

test_build()
#test_search()

