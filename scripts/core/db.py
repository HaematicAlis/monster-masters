card_dict = {}

def get_card_dict():
    return card_dict

def init_card_dict(cards):
    global card_dict
    card_dict = cards

def search_card_by_id(card_id):
    global card_dict
    if card_id not in card_dict:
        return None
    
    return card_dict[card_id] 
