from game.deck_util import draw
from game.view import view_deck, view_hand, view_status
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

        self.phase = "draw"

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
                print("Zone commands: deck, hand")
                print("Deck commands: draw")
                print("Phase commands: start, main, combat, war, end")
                print("Game commands: player, status")
                print("Other commands: exit, help")
            elif cmd == "status":
                view_status(self)
            elif cmd == "main":
                self.phase = "main"
                print("Phase set to Main")
            elif cmd == "combat":
                self.phase = "combat"
                print("Phase set to Combat")
            elif cmd == "war":
                self.phase = "war"
                print("Phase set to War")
            elif cmd == "end":
                self.phase = "end"
                print("Phase set to End")
            elif cmd == "start":
                self.phase = "draw"
                print("Phase set to Draw")
            else:
                print("! Command not found. Type 'help' for available commands.")
