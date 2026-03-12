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

def play_card(game, args):
    player = game.cur_player
    if player.hand_zone.size() == 0:
        print("! No cards in hand.")
        return
    if player.fight_zone.size() == 1:
        print("! Card already in Fight Zone")
        return

    if len(args) > 1 or args == []:
        print("! Usage: play <card_index>")
        return
    
    if not valid_hand_card(player, args[0]):
        return
    
    card_index = int(args[0])
    card = player.hand_zone.cards[card_index]
    player.hand_zone.move(card_index, player.fight_zone)
    print(f"{player.name} played {card.name}")
