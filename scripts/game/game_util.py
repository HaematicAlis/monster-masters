def change_phase(game, args):
    if len(args) != 1:
        print("! Usage: phase <phase_name>")
        return

    valid_phases = ["draw", "main", "combat", "war", "end"]
    phase = args[0]

    if phase not in valid_phases:
        print("! Invalid phase. (Valid phases: draw, main, combat, war, end)")
        return

    game.phase = phase
    print(f"Changed phase to {phase}")

def win_round(game):
    winner = game.cur_player
    for player in game.players.values():
        if player.fight_zone.size() > 0:
            player.fight_zone.move(0, winner.recycle_zone)
    print(f"Moved all cards to {winner}'s Recycle Pile.")
