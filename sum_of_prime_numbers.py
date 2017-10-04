import math
def sumOfPrimeNumbers(Range):
    """
    Returns the sum of all prime number bellow Range
    Range in an integer
    """
    listOfPrime=[2]
    i=3
    while i<Range:
        for a in listOfPrime:
            if i%a==0:
                break
            elif a>math.sqrt(i):
                listOfPrime.append(i)
                break
        i+=2
    return sum(listOfPrime)