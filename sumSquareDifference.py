def sumSquareDifference(Range):
    a=0
    b=0
    for i in range(Range+1):
        a+=i**2
        b+=i
    return(b**2-a)