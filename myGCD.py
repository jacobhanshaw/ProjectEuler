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
