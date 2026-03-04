def valid_num_cards(cmd, max_cards):
    if cmd == "":
        return False
    if not cmd.isdigit():
        print("! Enter a number.")
        return False
    if int(cmd) > max_cards:
        print("! Not enough cards in deck.")
        return False
    return True

def move_from_topdeck(game, zone, args):
    player = game.cur_player
    
    if args == []:
        if player.deck_zone.size() > 0:
            num_cards = 1
        else:
            print("! Not enough cards in deck.")
            return
    elif not valid_num_cards(args[0], player.deck_zone.size()):
        return
    else:
        num_cards = int(args[0])

    for i in range(num_cards):
        top_card = player.deck_zone.size() - 1
        player.deck_zone.move(top_card, zone)
    print(f"{player.name} moved {num_cards} cards from deck to {zone.name}.")

def draw(game, args):
    if len(args) > 1:
        print("! Usage: draw [num_cards]")
        return
    move_from_topdeck(game, game.cur_player.hand_zone, args)

def recycle_top(game, args):
    if len(args) > 1:
        print("! Usage: mill [num_cards]")
        return
    move_from_topdeck(game, game.cur_player.recycle_zone, args)

def return_to_deck(game, args):
    player = game.cur_player
    if player.hand_zone.size() == 0:
        print("! No cards in hand.")
        return
 
    if len(args) > 2 or args == []:
        print("! Usage: return <index_to_move> [destination_index]")
        return

    if len(args) == 1:
        destination = player.deck_zone.size()
    else:
        if not valid_num_cards(args[1], player.deck_zone.size()):
            return            
        destination = args[1]

    if not valid_num_cards(args[0], player.hand_zone.size() - 1):
        return
    card_index = args[0]

    card_to_move = player.hand_zone.cards[int(card_index)]
    if int(destination) == player.deck_zone.size():
        confirmation = input(f"Move {card_to_move.name} to top of deck? (y/n)\n> ").lower()
    else:
        confirmation = input(f"Move {card_to_move.name} into deck index {destination}? (y/n)\n> ").lower()
    if confirmation != "y":
        return
    player.hand_zone.move(int(card_index), player.deck_zone, int(destination))
    print(f"Moved {card_to_move.name} to index {destination}.")

def shuffle(game):
    game.cur_player.deck_zone.shuffle()
    print("Shuffled deck.")

# Empty deck restriction here temporarily; should be moved to game logic
def refresh_deck(game):
    player = game.cur_player
    if player.deck_zone.size() > 0:
        print("! Deck must be empty.")
        return
    player.deck_zone.cards = list(player.recycle_zone.cards)
    player.recycle_zone.cards = []
    shuffle(game)
