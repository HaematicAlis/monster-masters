from engine.db import get_card_dict

def search_card_by_id(card_id):
    card_dict = get_card_dict()
    if card_id not in card_dict:
        return None
    
    return card_dict[card_id] 
