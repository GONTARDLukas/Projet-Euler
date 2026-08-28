sumPrime=2
for i in range(3,2000000,2):
    isPrime=True
    for y in range(2,(int)(i**0.5+1)):
        if i%y==0:
            isPrime=False
    if isPrime:
        print(i)
        sumPrime+=i
print(sumPrime)