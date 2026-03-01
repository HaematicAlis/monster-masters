def valid_hand_card(player, cmd):
    if cmd == "":
        return False
    if not cmd.isdigit():
        print("! Enter a number.")
        return False
    if int(cmd) >= player.hand_zone.size():
        print("! Card not in hand.")
        return False
    return True

def play_card(game):
    player = game.cur_player
    
    print(player.hand_zone)
    print("Select card index:")
    cmd = ""
    while not valid_hand_card(player, cmd):
        cmd = input("> ")
    
    index = int(cmd)
    card = player.hand_zone.cards[index]
    player.hand_zone.move(index, player.fight_zone)
    print(f"{player} played {card.name}")
