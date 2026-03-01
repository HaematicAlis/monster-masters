def valid_num_cards(cmd, max_cards):
    if cmd == "":
        return False
    if not cmd.isdigit():
        print("! Enter a number.")
        return False
    if int(cmd) > max_cards:
        print("! Too many cards to draw.")
        return False
    return True

def move_from_topdeck(game, zone, num_cards):
    player = game.cur_player

    print("# of cards:")
    if num_cards == None:
        cmd = ""
        while not valid_num_cards(cmd, player.deck_zone.size()):
            cmd = input("> ")
        num_cards = int(cmd)

    for i in range(num_cards):
        top_card = player.deck_zone.size() - 1
        player.deck_zone.move(top_card, zone)
    print(f"{player.name} moved {num_cards} cards from deck to {zone.name}.")

def draw(game, num_cards=None):
    move_from_topdeck(game, game.cur_player.hand_zone, num_cards)

def recycle_top(game, num_cards=None):
    move_from_topdeck(game, game.cur_player.recycle_zone, num_cards)
