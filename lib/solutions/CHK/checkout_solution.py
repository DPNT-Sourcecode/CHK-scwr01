

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
        "A":(3,130),
        "B":(2,45)
    }
    
    

def checkout(skus):
    """checkout supermarkt checkout and calculate the total prices

    Args:
        skus (str): all product skus

    Returns:
        Integer: total prices
    """
    prices=get_prices()
    offers=get_offers()
    
    
    if validate_skus(skus,prices):
        return -1
    
    return 123


