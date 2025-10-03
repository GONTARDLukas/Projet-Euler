def generatePrime(n):
    primes = [2]
    i=3


    while len(primes)<n:
        isPrime=True
        for prime in primes:
            if(prime**2>i):
                break
            if(i%prime==0):
                isPrime=False
                break
        if(isPrime):
            primes+=[i]
        i+=2
    return primes[len(primes)-1]

def findGPD(n):#greatest prime divisor 
    primes = [2]
    divisor=[]
    i=3
    while len(primes)<n:
        isPrime=True
        for prime in primes:
            if(prime**2>i):
                break
            if(i%prime==0):
                isPrime=False
                break
        if(isPrime):
            primes+=[i]
        while(n%i==0):
            n/=i
            divisor+=[i]
        i+=2
    return divisor
print(findGPD(600851475143))