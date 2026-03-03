from engine.card import Card
import random
class Zone:
    def __init__(self, name, owner, visibility=set()):
        self.name = name
        self.owner = owner
        self.cards = []
        self.visibility = visibility
    
    def __str__(self):
        zone_list = f"[Zone: {self.name}] ({len(self.cards)}) vis: {self.visibility}"
        for card in self.cards:
            zone_list += "\n"
            zone_list += f"[{str(self.cards.index(card))}]"
            zone_list += str(card)
        return zone_list

    def size(self):
        return len(self.cards)

    # TODO: Untested since change to set
    def reveal_to_player(self, pid):
        self.visibility.add(pid)
        for card in self.cards:
            card.visibility.add(pid)
    
    # TODO: Untested since change to set
    def hide_from_player(self, pid):
        self.visibility.remove(pid)
        for card in self.cards:
            card.visibility.remove(pid)

    # Not currently needed
    #def find_by_uid(self, uid):
    #    for card in self.cards:
    #        if card.uid == uid:
    #            return self.cards.index(card)
    #    return None
    #
    #def remove_by_uid(self, uid):

    def find_by_set_id(self, set_id):
        for card in self.cards:
            if card.set_id == set_id:
                return self.cards.index(card)
        return None

    # Maybe change default index
    def add(self, card_info, index=-1):
        if index == -1:
            index = len(self.cards)
        card_to_add = Card(card_info, self)
        self.cards.insert(index, card_to_add)

    def remove(self, index):
        if index < 0 or index >= len(self.cards):
            print("! Remove: Index out of bounds")
            return
        self.cards.pop(index)

    # index -> index of current zone to move from
    # zone -> zone to move to
    # add_index -> index in destination zone (optional; default is end of zone)
    # Maybe refactor
    # Maybe change default index
    # TODO: Visibility untested after change to set
    def move(self, index, zone, add_index=-1):
        if add_index == -1:
            add_index = len(zone.cards)
        if index < 0 or index >= len(self.cards):
            print("! Move: Index out of bounds")
            return
        card = self.cards[index]
        card.zone = zone.name
        card.owner = zone.owner
        card.visibility = set(zone.visibility)
        zone.cards.insert(add_index, card)
        self.remove(index)

    def shuffle(self):
        random.shuffle(self.cards)
