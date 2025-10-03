def fibobo(n, l={0:1,1:1}):
    if(n not in l):
        l[n] = fibobo(n-1,l)[n-1]+fibobo(n-2,l)[n-2]
    return l
def fibobo(max):
    U0=1
    Un=1    
    termes=[U0,Un]
    while(termes[len(termes)-1]<max):
        termes.append(termes[len(termes)-1]+termes[len(termes)-2])
    return termes
max=4000000
print(sum(i if i%2==0 else 0 for i in fibobo(max)))