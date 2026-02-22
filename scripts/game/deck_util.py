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

def draw(game, num_cards=None):
    player = game.cur_player

    if num_cards == None:
        cmd = ""
        while not valid_num_cards(cmd, len(player.deck_zone.cards)):
            cmd = input("> ")
        num_cards = int(cmd)

    for i in range(num_cards):
        top_card = len(player.deck_zone.cards) - 1
        player.deck_zone.move(top_card, player.hand_zone)
    print(f"{player.name} drew {num_cards} cards.")
