def valid_player(game, pid):
    if not pid.isdigit():
        print("! Enter a number.")
        return False
    if int(pid) not in game.players:
        print("! Player not found")
        return False
    return True

def view_deck(game, args):
    if args == []:
        print(game.cur_player.deck_zone)
        return
    elif len(args) > 1:
        print("! Usage: deck [pid]")
        return
    if valid_player(game, args[0]):
        pid = int(args[0])
        print(game.players[pid].deck_zone)

def view_hand(game, args):
    if args == []:
        print(game.cur_player.hand_zone)
        return
    elif len(args) > 1:
        print("! Usage: hand [pid]")
        return
    if valid_player(game, args[0]):
        pid = int(args[0])
        print(game.players[pid].hand_zone)

def view_recycle(game, args):
    if args == []:
        print(game.cur_player.recycle_zone)
        return
    elif len(args) > 1:
        print("! Usage: recycle [pid]")
        return
    if valid_player(game, args[0]):
        pid = int(args[0])
        print(game.players[pid].recycle_zone)

def view_fight(game, args):
    if args == []:
        print(game.cur_player.fight_zone)
        return
    elif len(args) > 1:
        print("! Usage: fight [pid]")
        return
    if valid_player(game, args[0]):
        pid = int(args[0])
        print(game.players[pid].fight_zone)

def view_special(game, args):
    if args == []:
        print(game.cur_player.special_zone)
        return
    elif len(args) > 1:
        print("! Usage: special [pid]")
        return
    if valid_player(game, args[0]):
        pid = int(args[0])
        print(game.players[pid].special_zone)

def view_discard(game, args):
    print(game.discard_zone)

def view_ante(game, args):
    print(game.ante_zone)

def view_help():
    print("View commands: deck, hand, recycle, special, ante, fight, status, board")
    print("Deck commands: draw, mill, shuffle, return")
    print("Hand commands: play")
    print("Player commands: player")
    print("Game commands: phase, win")
    print("Other commands: exit, help, clear")

def view_board(game):
    for player in game.players.values():
        if player.fight_zone.size() == 0:
            print(f"{player.name}: empty")
        else:
            print(f"{player.name}: {player.fight_zone.cards[0]}")

def view_status(game):
    for player in game.players.values():
        deck_size = player.deck_zone.size()
        hand_size = player.hand_zone.size()
        recycle_size = player.recycle_zone.size()
        special_size = player.special_zone.size()
        print(f"{player} - D:{deck_size} H:{hand_size} R:{recycle_size} S:{special_size}")
    print(f"Phase: {game.phase}")
    print(f"Current player: {game.cur_player}")
