from systems.deck_util import draw, recycle_top, shuffle, return_to_deck, refresh_deck
from systems.view import view_zone, view_help, view_board, view_status
from systems.player_util import switch_player
from systems.hand_util import play_card
from systems.game_util import change_phase, win_round
from core.zone import Zone
from core.board import Board

largest_gid = 0

class Game:
    def __init__(self, players):
        global largest_gid
        largest_gid += 1
        self.gid = largest_gid

        self.players = players
        self.num_players = len(players)
        if self.num_players > 0:
            self.cur_player = next(iter(players.values()))

        # BOARD WIP
        self.board = Board(self)

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

        shuffle(self, ["all"])
        change_phase(self, ["draw"])

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
                switch_player(self, args)
            elif cmd == "view":
                view_zone(self, args)
            elif cmd == "play":
                play_card(self, args)
            elif cmd == "exit":
                print("Goodbye!")
            elif cmd == "help":
                view_help()
            elif cmd == "board":
                view_board(self)
            elif cmd == "status":
                view_status(self)
            elif cmd == "phase":
                change_phase(self, args)
            elif cmd == "win":
                win_round(self)
            elif cmd == "return":
                return_to_deck(self, args)
            elif cmd == "shuffle":
                shuffle(self, args)
            elif cmd == "refresh":
                refresh_deck(self)
            else:
                print("! Command not found. Type 'help' for available commands.")
