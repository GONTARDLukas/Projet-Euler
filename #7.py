def searchNthPrime(primeList=[2],n=3):
    currentNumber=max(primeList)+1
    while len(primeList)<n:
        isPrime=True
        for i in primeList:
            if currentNumber%i==0:
                isPrime=False
                break
        if isPrime:
            primeList+=[currentNumber]
        currentNumber+=2
    return primeList
print(searchNthPrime([2],10001))