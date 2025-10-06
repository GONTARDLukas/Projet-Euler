def palindromProduct(n):
    palindrom = []
    for i in range(10**n, 10**(n+1)):
        for y in range(10**n, 10**(n+1)):
            if isPalindrom(str(i*y)):
                palindrom+=[(i,y)]
    return palindrom
def isPalindrom(x):
    print(x)
    if(len(x)%2==1):
        x =x[:(len(x))//2]+x[(len(x))//2+1:]
    print(x)
    isPalindrom=True
    for i in range(len(x)//2):
        if x[i] != x[len(x)-i-1]:
            print(x[i], x[len(x)-i-1],x)
            isPalindrom = False
            break
    if isPalindrom:
        print(x, "True")
    return isPalindrom
print(isPalindrom("aabaa"))
print(palindromProduct(1))


print(isPalindrom(str(99*91)))