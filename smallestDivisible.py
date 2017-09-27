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

#More efficient solution to this problem
def smallestMultiple(Range):
    """Returns a smallest number that can be evenly
    divisible by the numbers within a range
    For Example 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    """
    value={}
    value_copy=value.copy()
    for b in range(2,Range+1):
        def primeFactors(i):
            if i==1:
                return value
            else:
                a=2
                while True:
                    if i%a==0:
                        value[a]=value.get(a,0)+1
                        return primeFactors(i//a)
                    a+=1
        primeFactors(b)
        for a in value:
            if value[a]>value_copy.get(a,0):
                value_copy[a]=value[a]
        value={}
    ans=1
    for i in value_copy:
        ans*=i**value_copy[i]
    return ans

#More More efficient solution to this problem

def smallestMultiple(Range):
    """Returns a smallest number that can be evenly
    divisible by the numbers within a range
    For Example 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    """
    i = 1
    for k in (range(1, Range+1)):
        if i % k > 0:
            for j in range(1, Range+1):
                if (i*j) % k == 0:
                    i *= j
                    break
    return i
