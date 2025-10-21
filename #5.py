def findSmalestNumberByMultiples(rangeOfMultiples):
    concatenatedMultiples = {}
    for i in range(rangeOfMultiples):
        primeMultiplesOfN = decompose(i)
        for multiple in primeMultiplesOfN:
            if (multiple in concatenatedMultiples and primeMultiplesOfN[multiple]>concatenatedMultiples[multiple]) or multiple not in concatenatedMultiples:
                concatenatedMultiples[multiple]=primeMultiplesOfN[multiple]
    return concatenatedMultiples
def decompose(number):
    multiples={}
    for i in range(2,number):
        while number%i==0:
            if i in multiples:
                multiples[i]+=1
            else:
                multiples[i]=1
            number/=i
    return multiples
def recomposeNumber(multiples):
    number=1
    for NMultiple in multiples:
        number*=NMultiple**multiples[NMultiple]
    return number
print(findSmalestNumberByMultiples(10))
print(decompose(2520))
print(recomposeNumber(findSmalestNumberByMultiples(10)))