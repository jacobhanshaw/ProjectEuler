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

def totient(n):
    factors=primeFactors(n)
    result=n
    for key in factors:
        result*=1-float(1)/float(key)
            
    return result

for i in range(2,11):
    print totient(i)

"""
maxValue=3
maxFraction=1.67

for n in range(11,1000001):
    fraction=float(n)/float(totient(n))
    if fraction > maxFraction:
        print "F:",fraction,"N:",n
        maxFraction=fraction
        maxValue=n

print "Result: ",maxValue
"""

print "Result:",(2*3*5*7*11*13*17)
