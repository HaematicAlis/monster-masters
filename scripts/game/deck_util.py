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

def return_to_deck(game):
    player = game.cur_player
    confirmation = ""
    if player.hand_zone.size() == 0:
        print("No cards in hand.")
        return
    while confirmation != "y":
        print(player.hand_zone)
        target_card = input("Enter card index you would like to move:\n> ")
        if not valid_num_cards(target_card, player.hand_zone.size() -1):
            return
        card_index = player.hand_zone.cards[int(target_card)]
        print(player.deck_zone)
        destination = input("Enter deck index:\n> ")
        if not valid_num_cards(destination, player.deck_zone.size() -1):
            return
        confirmation = input(f"Move {card_index.name} into deck index {destination}? (y/n)\n").lower()
    player.hand_zone.move(int(target_card), player.deck_zone, int(destination))
    print(f"Moved {card_index.name} to index {destination}")


def shuffle(game):
    game.cur_player.deck_zone.shuffle()
    print("Shuffled deck.")
