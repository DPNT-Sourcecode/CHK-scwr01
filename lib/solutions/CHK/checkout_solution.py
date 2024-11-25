

from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def get_prices()->dict:
    """get_prices generate methods

    Returns:
        dict: prices
    """
    return {
        "A":50,
        "B":30,
        "C":20,
        "D":15,
        "E":40
    }

def get_offers()->dict:
    """get_offers generate methods

    Returns:
        dict: offers
    """
    return {
        "A":[(3,130),(5,200)],
        "B":[(2,45)]
    }

def get_free()->dict:
    """get_free get few 2E one B free

    Returns:
        dict: _description_
    """
    return {
        "E":(2,"B")
    }
def validate_skus(skus,prices) ->bool:
    """validate_skus validate skus

    Args:
        skus (str): _description_
        prices (dict): _description_

    Returns:
        bool: _description_
    """
    return all(item in prices for item in skus)


def apply_free_offer(items,item,free_item,free_count):
    """apply_free_offer calculate free items and excluse them
    """
    if items[item] >= free_count:
        deduct_item = items[item] // free_count
        items[free_item] =max(0,items[free_item]-deduct_item)
        
def checkout(skus):
    """checkout supermarkt checkout and calculate the total prices

    Args:
        skus (str): all product skus

    Returns:
        Integer: total prices
    """
    prices=get_prices()
    offers=get_offers()
    free_offers= get_free()
    
    if not isinstance(skus,str) or not validate_skus(skus,prices):
        return -1
    
    
    
    items=Counter(skus)
    
    for item,offer in free_offers.items():
        if isinstance(offer,tuple) and offer[1] in prices:
            apply_free_offer(items,item,offer[1],offer[2])
        
        
    
    total_price=0
    for item, count in items.items():
        if item in offers:
            for offer in sorted(offers[item],key=lambda x: -x[0]):
                offer_qty,offer_price=offer
                offer_used=count//offer_qty
                
                left_times = count%offer_qty
                total_price += offer_used * offer_price + left_times * prices[item]
        else:
            total_price += count*prices[item]
            
    return total_price

