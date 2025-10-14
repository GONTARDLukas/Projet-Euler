sumOfTheFirstN = lambda n:n*(n+1)/2
sumOfTheFirstSquaredN = lambda n:n*(n+1)*(2*n+1)/6
print(sumOfTheFirstN(100)**2)
print(sumOfTheFirstSquaredN(100))
print(sumOfTheFirstN(100)**2-sumOfTheFirstSquaredN(100))