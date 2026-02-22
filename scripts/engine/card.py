largest_uid = 0
created_cards = {}

class Card:
    def __init__(self, card_info, zone):
        global largest_uid
        global created_cards

        largest_uid += 1
        self.uid = largest_uid

        self.set_id = card_info["set_id"]
        self.name = card_info["name"]
        self.level = card_info["level"]
        self.typeline = card_info["typeline"]
        self.abilities = card_info["abilities"]
        self.rarity = card_info["rarity"]
        self.color = card_info["color"]
        self.cost = card_info["cost"]

        self.zone = zone.name
        self.owner = zone.owner
        self.visibility = list(zone.visibility)

        created_cards[self.uid] = self

    def __str__(self):
        return f"UID{self.uid}: {self.name}, L{self.level} {self.typeline} ({self.rarity})\nAbilities: {self.abilities}"

    def reveal_to_player(self, pid):
        if pid in self.visibility:
            return
        self.visibility.append(pid)
        print(f"DEBUG: Appending {pid} to {self.name} (from CARD); vis: {self.visibility}")

    def hide_from_player(self, pid):
        if pid not in self.visibility:
            return
        index_to_hide = self.visibility.index(pid)
        self.visibility.pop(index_to_hide)
