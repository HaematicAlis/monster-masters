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
    elif len(args) > 2:
        print("! Usage: deck [pid]")
        return
    if valid_player(game, args[0]):
        pid = int(arg[0])
        print(game.players[pid].deck_zone)

# TODO: Add args code from deck to other zones
def view_hand(game, args):
    print(game.cur_player.hand_zone)

def view_recycle(game, args):
    print(game.cur_player.recycle_zone)

def view_special(game, args):
    print(game.cur_player.special_zone)

def view_discard(game, args):
    print(game.discard_zone)

def view_ante(game, args):
    print(game.ante_zone)

def view_fight(game, args):
    print(game.cur_player.fight_zone)

def view_help():
    print("View commands: deck, hand, recycle, special, ante, fight, status")
    print("Deck commands: draw, mill, shuffle")
    print("Hand commands: play")
    print("Player commands: player")
    print("Phase commands: start, main, combat, war, end")
    print("Other commands: exit, help, clear")

def view_status(game):
    for player in game.players.values():
        deck_size = player.deck_zone.size()
        hand_size = player.hand_zone.size()
        recycle_size = player.recycle_zone.size()
        special_size = player.special_zone.size()
        print(f"{player} - D:{deck_size} H:{hand_size} R:{recycle_size} S:{special_size}")
    print(f"Phase: {game.phase}")
    print(f"Current player: {game.cur_player}")
