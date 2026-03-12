from entities.card import Card
from util.files import import_cards, import_decklist
from core.db import init_card_dict
from entities.player import Player
from core.game import Game

CARD_DATA_PATH = "data/cards.csv"
TEST_DECK = "decks/test.deck"

def main():
    card_dict = import_cards(CARD_DATA_PATH)
    init_card_dict(card_dict)
    
    p1 = Player("p1", 1)
    p2 = Player("p2", 2)
    
    test_deck1 = import_decklist(TEST_DECK)
    test_deck2 = import_decklist(TEST_DECK)
    test_deck1.build(p1.deck_zone)
    test_deck2.build(p2.deck_zone)
 
    game = Game({1:p1, 2:p2})
    game.game_loop()

main()
