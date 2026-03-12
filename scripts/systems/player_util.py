def valid_player(cmd, players):
    if cmd == "":
        return False
    if not cmd.isdigit():
        print("! Enter a number.")
        return False
    if int(cmd) not in players:
        print("! Player not in game")
        return False
    return True

def show_pids(game):
    print("[", end="")
    for pid in game.players:
        if pid == game.cur_player.pid:
            print(f" > {pid} < ", end="")
        else:
            print(f" {pid} ", end="")
    print("]")

def switch_player(game, args):
    if len(args) > 1:
        print("! Usage: player [pid]")
        return
    if len(args) == 1:
        if not valid_player(args[0], game.players):
            return
        pid = int(args[0])
    else:
        cmd = ""
        print("Enter PID to switch to:")
        show_pids(game)

        while not valid_player(cmd, game.players):
            cmd = input("> ")
        pid = int(cmd)

    new_player = game.players[pid]
    game.cur_player = new_player
    show_pids(game)
    print(f"Switched to {new_player.name}.")
