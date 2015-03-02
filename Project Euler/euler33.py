from fractions import gcd
from math import sqrt

def primeFactors(num):

    if num == 0:
        return {}

    factors={}
    startNum=num

    while num % 2 == 0:
        factors[2]=factors.get(2,0)+1
        num /= 2
        
    i=3
    maxPos=sqrt(num)

    while i <= maxPos:
        
        if num % i == 0:
            factors[i]=factors.get(i,0)+1
            num /= i
        else:
            i+=2

    if num > 1: 
        factors[num]=factors.get(num,0)+1

    return factors

def myGCD(a,b):
    factorsA=primeFactors(a)
    factorsB=primeFactors(b)

    r = dict([(k, min(factorsA[k],factorsB[k])) for k in set(factorsA) & set(factorsB)])

    result=1

    for num in r:
        result*=(num**r[num])
    
    return result

numProd=1
denomProd=1

for denom in range(99,10,-1):
    for num in range(denom-1,9,-1):
        fraction = float(num)/float(denom)
        numDiv = float(num // 10)
        numMod = float(num  % 10)
        denomDiv = float(denom // 10)
        denomMod = float(denom  % 10)

        if denomDiv <> 0:
            if numDiv == denomMod and fraction == (numMod/denomDiv):
                numProd*=numMod
                denomProd*=denomDiv
            elif denomMod <> 0 and numMod == denomMod and fraction == (numDiv/denomDiv):
                numProd*=numDiv
                denomProd*=denomDiv
        if denomMod <> 0:               
            if  numDiv == denomDiv and fraction == (numMod/denomMod):
                numProd*=numMod
                denomProd*=denomMod
            elif numMod == denomDiv and fraction == (numDiv/denomMod):
                numProd*=numDiv
                denomProd*=denomMod
                
print "Result: ",(denomProd/gcd(numProd,denomProd))

print "My GCD Result: ",(denomProd/myGCD(numProd,denomProd))
