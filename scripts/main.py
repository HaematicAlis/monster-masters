from engine.card import Card
from engine.files import import_cards, import_decklist
from engine.db import init_card_dict
from engine.player import Player
from game.game import Game

CARD_DATA_PATH = "data/cards.csv"
TEST_DECK = "decks/test.deck"

def main():
    card_dict = import_cards(CARD_DATA_PATH)
    init_card_dict(card_dict)
    
    p1 = Player("p1", 1)
    p2 = Player("p2", 2)
    
    game = Game([p1, p2])

    test_deck1 = import_decklist(TEST_DECK)
    test_deck2 = import_decklist(TEST_DECK)
    test_deck1.build(p1.deck_zone)
    test_deck2.build(p2.deck_zone)
    
    game.game_loop()

main()
