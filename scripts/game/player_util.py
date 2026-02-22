def find_player(pid, players):
    for player in players:
        if player.pid == pid:
            return player
    return None

def valid_player(cmd, players):
    if cmd == "":
        return False
    if not cmd.isdigit():
        print("! Enter a number.")
        return False
    if find_player(int(cmd), players) == None:
        print("! Player not in game")
        return False
    return True

def show_pids(game):
    print("[", end="")
    for player in game.players:
        if player == game.cur_player:
            print(f" > {player.pid} < ", end="")
        else:
            print(f" {player.pid} ", end="")
    print("]")

def switch_player(game):
    cmd = ""
    print("Enter PID to switch to:")
    show_pids(game)

    while not valid_player(cmd, game.players):
        cmd = input("> ")
    pid = int(cmd)

    new_player = find_player(pid, game.players)
    game.cur_player = new_player
    show_pids(game)
    print(f"Switched to {new_player}.")
