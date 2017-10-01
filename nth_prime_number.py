import math
def nthPrimeNumber(Range):
    """
    This function returns an nth prime number.
    Range is an integer value which is passed
    by the user of this function.
    """
    primeNumbers=[2]
    b=3
    while len(primeNumbers)<Range:
        for a in primeNumbers:
            if b%a==0:
                break
            elif a>math.sqrt(b):
                primeNumbers.append(b)
                break
        b+=2
    return primeNumbers[-1]
