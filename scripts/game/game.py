from game.deck_util import draw, recycle_top, shuffle, return_to_deck
from game.view import view_deck, view_hand, view_status, view_recycle, view_special, view_discard, view_ante, view_fight, view_help
from game.player_util import switch_player
from game.hand_util import play_card
from engine.zone import Zone

largest_gid = 0

class Game:
    def __init__(self, players):
        global largest_gid

        self.players = players
        if len(players) > 0:
            self.cur_player = next(iter(players.values()))

        largest_gid += 1
        self.gid = largest_gid

        self.phase = "draw"

        # Reveal public player zones to all other players
        for player in self.players.values():
            for pid in self.players:
                player.fight_zone.reveal_to_player(pid)
                player.special_zone.reveal_to_player(pid)
                player.recycle_zone.reveal_to_player(pid)

        player_ids = set(self.players.keys())
        self.discard_zone = Zone("discard", 0, player_ids)
        self.ante_zone = Zone("ante", 0, player_ids)

        # Reveal public zones to all players 
        for pid in self.players:
            self.discard_zone.reveal_to_player(pid)
            self.ante_zone.reveal_to_player(pid)

    def __str__(self):
        s = f"GID{self.gid}: Players["
        for pid in self.players:
            s += f"PID{pid}:{players[pid].name};"
        s += "]"
        return s

    def game_loop(self):
        cmd = ""
        while cmd != "exit":
            line = input("> ")
            tokens = line.split(" ")
            cmd = tokens[0]
            if len(tokens) > 1:
                args = tokens[1:]
            else:
                args = []

            if cmd == "draw":
                draw(self, args)
            elif cmd == "mill":
                recycle_top(self, args)
            elif cmd == "clear":
                for i in range(30):
                    print("")
            elif cmd == "player":
                switch_player(self)
            elif cmd == "deck":
                view_deck(self, args)
            elif cmd == "hand":
                view_hand(self, args)
            elif cmd == "recycle":
                view_recycle(self, args)
            elif cmd == "special":
                view_special(self, args)
            elif cmd == "discard":
                view_discard(self, args)
            elif cmd == "ante":
                view_ante(self, args)
            elif cmd == "fight":
                view_fight(self, args)
            elif cmd == "play":
                play_card(self)
            elif cmd == "exit":
                print("Goodbye!")
            elif cmd == "help":
                view_help()
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
            elif cmd == "return":
                return_to_deck(self)
            elif cmd == "shuffle":
                shuffle(self)
            else:
                print("! Command not found. Type 'help' for available commands.")
