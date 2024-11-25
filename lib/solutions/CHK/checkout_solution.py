

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
        "B":[(2,45)], 
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

def apply_prices_offer(item,count,offers,prices):
    total=0
    if item in offers:
        for offer in sorted(offers[item],key=lambda x: -x[0]):
            offer_qty,offer_price=offer
            offer_used=count//offer_qty
            total += offer_used +offer_price
             
            
    else:
    total_price += count*prices[item]

    return total_price

            
def checkout(skus):
    """checkout supermarkt checkout and calculate the total prices

    Args:
        skus (str): all product skus

    Returns:
        Integer: total prices
    """
    prices=get_prices()
    offers=get_offers()
    
    if not isinstance(skus,str) or not validate_skus(skus,prices):
        return -1
    
    
    
    items=Counter(skus)
    
    for item,offer in offers.items():
        if isinstance(offer,tuple) and offer[1] in prices:
            apply_free_offer(items,item,offer[1],offer[0])
        
        
    
    total_price=0
    for item, count in items.items():
        if item in offers and isinstance(offers[item],list):
            total_price+=apply_prices_offer(item,count,offers,prices)
        else:
            total_price+=count*prices[item]
    return total_price


