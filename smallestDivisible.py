def smallestMultiple(Range):
    """Returns a smallest number that can be evenly
    divisible by the numbers within a range
    For Example 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    """
    number=Range
    while True:
        for i in range(1,Range+1):
            if number%i!=0:
                number+=Range
                break
            elif i==Range:
                return number        