

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
        "D":15
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
    
    
def validate_skus(skus,prices) ->bool:
    """validate_skus validate skus

    Args:
        skus (str): _description_
        prices (dict): _description_

    Returns:
        bool: _description_
    """
    return all(item in prices for item in skus)

def checkout(skus):
    """checkout supermarkt checkout and calculate the total prices

    Args:
        skus (str): all product skus

    Returns:
        Integer: total prices
    """
    prices=get_prices()
    offers=get_offers()
    
    
    if not validate_skus(skus,prices):
        return -1
    
    items=Counter(skus)
    
    total_price=0
    for item, count in items.items():
        if item in offers:
            offer_qty,offer_price=offers[item]
            offer_used=count//offer_qty
            left_times = count%offer_qty
            total_price += offer_used * offer_price + left_times * prices[item]
        else:
            total_price += count*prices[item]
            
    return total_price

