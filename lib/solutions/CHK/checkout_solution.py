

from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def get_prices()->dict:
    """get_prices generate methods

    Returns:
        dict: prices
    """
    return {
        "A": 50, "B": 30, "C": 20, "D": 15, "E": 40,
        "F": 10, "G": 20, "H": 10, "I": 35, "J": 60,
        "K": 70, "L": 90, "M": 15, "N": 40, "O": 10,
        "P": 50, "Q": 30, "R": 50, "S": 20, "T": 20,
        "U": 40, "V": 50, "W": 20, "X": 17, "Y": 20, "Z": 21
    }

def get_offers()->dict:
    """get_offers generate methods

    Returns:
        dict: offers
    """
    return {
        "A":[(3,130),(5,200)],
        "B":[(2,45)], 
        "E":(2,"B"),
        "F":(3,"F"),
        "H":[(10,80),(5,45)],
        "K":[(2,150)],
        "N":(3,"M"),
        "P":[(5,200)],
        "Q":[(3,80)],
        "R":(3,"Q"),
        "U":(4,"U"),
        "V":[(3,130),(2,90)],
        "S":[(3,45)],
        "T":[(3,45)],
        "Y":[(3,45)],
        "Z":[(3,45)]
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
    """apply_prices_offer apply mutiple item different prices offers

    Args:
        item (_type_): _description_
        count (_type_): _description_
        offers (_type_): _description_
        prices (_type_): _description_

    Returns:
        _type_: _description_
    """
    total=0
    if item in offers:
        for offer in sorted(offers[item],key=lambda x: -x[0]):
            offer_qty,offer_price=offer
            offer_used=count//offer_qty
            total += offer_used *offer_price
            count %= offer_qty
    total += count*prices[item]

    return total

def apply_group_discount(items):
    group_item=["S","T","X","Y","Z"]
    group_count= sum(items[item] for item in group_item if item in items)
    if group_count >=3:
        group_discount_count=group_count//3
        group_price=45
        return group_discount_count * group_price
    return 0
            
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
        
        
    
    total_price=apply_group_discount(items,prices)
    for item, count in items.items():
        if item in offers and isinstance(offers[item],list):
            total_price+=apply_prices_offer(item,count,offers,prices)
        else:
            total_price+=count*prices[item]
    return total_price
