def greatestProduct(numbers):
    """
    Returns greatest product of 13 adjacent
    numbers from a set of numbers.
    if length of set is less then 13
    returns 0.
    """
    grtProduct=0
    for i in range(len(numbers)):
        product=1
        try:
            for a in range(i,i+13):
                product*=int(numbers[a])
            if product>grtProduct:
                grtProduct=product
        except:
            return grtProduct