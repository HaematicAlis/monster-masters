import db

def search_card_by_id(card_id):
    if card_id not in db.card_dict:
        return None
    
    return db.card_dict[card_id] 
