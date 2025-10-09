def findMultiple(n):
    multiples=[]
    for i in range(2,n-1):
        if n%i==0:
            multiples+=[i]
    return multiples + ([n] if len(multiples)==0 else [])
def findMultiples(interval):
    multiples=[]
    for i in interval:
        multiples+=findMultiple(i)
    multiples.sort()
    return multiples
def isMultiple(n, interval):
    for i in interval:
        if n%i!=0:
            return False
    return True
def smalestMultiple(interval):
    i=5
    while(not isMultiple(i, interval)):
        i+=5
    return i
print(findMultiples(range(1,10)))
print(smalestMultiple(range(1,10)))