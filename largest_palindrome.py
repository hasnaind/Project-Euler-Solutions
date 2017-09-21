def Largest_palindrome_product():
    largestPalindrome=None
    for i in range(999,99,-1):
        for a in range(999,99,-1):
            result=str(a*i)
            if result==result[::-1]:
                if largestPalindrome==None or int(result)>largestPalindrome:
                    largestPalindrome=int(result)
    return largestPalindrome