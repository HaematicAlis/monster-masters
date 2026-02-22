from game.deck_util import draw
from game.view import view_deck, view_hand
from game.player_util import switch_player

largest_gid = 0

class Game:
    def __init__(self, players):
        global largest_gid

        self.players = players
        if len(players) > 0:
            self.cur_player = players[0]

        largest_gid += 1
        self.gid = largest_gid

    def __str__(self):
        s = f"GID{self.gid}: Players["
        for player in self.players:
            s += f"PID{player.pid}:{player.name};"
        s += "]"
        return s

    def game_loop(self):
        cmd = ""
        while cmd != "exit":
            cmd = input("> ")
            if cmd == "draw":
                draw(self)
            elif cmd == "clear":
                for i in range(30):
                    print("")
            elif cmd == "player":
                switch_player(self)
            elif cmd == "deck":
                view_deck(self)
            elif cmd == "hand":
                view_hand(self)
            elif cmd == "exit":
                print("Goodbye!")
            elif cmd == "help":
                print("Available commands: deck, draw, exit, hand, help, player")
            else:
                print("! Command not found. Type 'help' for available commands.")
