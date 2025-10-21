def palindromProduct(n):
    palindrom = []
    for i in range(10**(n-1), 10**n):
        for y in range(10**(n-1), 10**n):
            if isPalindrom(str(i*y)):
                palindrom+=[(i,y)]
    return palindrom
def isPalindrom(x):
    if(len(x)%2==1):
        x =x[:(len(x))//2]+x[(len(x))//2+1:]
    isPalindrom=True
    for i in range(len(x)//2):
        if x[i] != x[len(x)-i-1]:
            isPalindrom = False
            break
    return isPalindrom
maxPalindromProduct = max(palindromProduct(3), key= lambda n:n[0]*n[1])
print(maxPalindromProduct[0]*maxPalindromProduct[1])
print(isPalindrom(str(99*91)))