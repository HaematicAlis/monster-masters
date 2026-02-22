from engine.zone import Zone

class Player:
    def __init__(self, name, pid):
        self.name = name
        self.pid = pid
        self.deck_zone = Zone(f"deck_{pid}", pid)
        self.hand_zone = Zone(f"hand_{pid}", pid)

    def __str__(self):
        return f"PID{self.pid}: {self.name}"
