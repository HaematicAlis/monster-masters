def search_card_by_id(card_dict, card_id):
    if card_id not in card_dict:
        return None
    
    return card_dict[card_id] 
