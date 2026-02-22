from engine.zone import Zone

class Player:
    def __init__(self, name, pid):
        self.name = name
        self.pid = pid
        self.deck_zone = Zone(f"deck_{pid}", pid)
        self.hand_zone = Zone(f"hand_{pid}", pid)
        self.recycle_zone = Zone(f"recycle_{pid}", pid)
        self.special_zone = Zone(f"special_{pid}", pid)
        self.fight_zone = Zone(f"fight_{pid}", pid)

    def __str__(self):
        return f"PID{self.pid}: {self.name}"
