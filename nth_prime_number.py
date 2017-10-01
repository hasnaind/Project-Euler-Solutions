import math
def nthPrimeNumber(Range):
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
