def view_deck(game):
    print(game.cur_player.deck_zone)

def view_hand(game):
    print(game.cur_player.hand_zone)

def view_recycle(game):
    print(game.cur_player.recycle_zone)

def view_special(game):
    print(game.cur_player.special_zone)

def view_discard(game):
    print(game.discard_zone)

def view_ante(game):
    print(game.ante_zone)

def view_fight(game):
    print(game.cur_player.fight_zone)

def view_help():
    print("View commands: deck, hand, recycle, special, ante, fight, status")
    print("Deck commands: draw, mill, shuffle")
    print("Hand commands: play")
    print("Player commands: player")
    print("Phase commands: start, main, combat, war, end")
    print("Other commands: exit, help, clear")

def view_status(game):
    for player in game.players:
        deck_size = player.deck_zone.size()
        hand_size = player.hand_zone.size()
        recycle_size = player.recycle_zone.size()
        special_size = player.special_zone.size()
        print(f"{player} - D:{deck_size} H:{hand_size} R:{recycle_size} S:{special_size}")
    print(f"Phase: {game.phase}")
    print(f"Current player: {game.cur_player}")
