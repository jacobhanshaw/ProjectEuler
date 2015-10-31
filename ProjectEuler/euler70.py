from fractions import gcd
from math import sqrt,floor

#Valid, but slow

def isPrime(n):
    if n % 2 == 0:
        return False
    elif n % 3==0:
        return False
    else:
        r=floor(sqrt(n)) # n rounded to the greatest integer r so that r*r<=n
        f=5
        while f<=r:
            if n % f==0:
                return False
            if n % (f+2) == 0:
                return False
            f=f+6

    return True

def getKey(num):
    numArr=[0] * 10

    for char in str(num):
        numArr[int(char)]+=1

    key=""
    for i in range(10):
        key+=str(numArr[i])

    return key

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

result=-1
minRatio=-1

for n in range(2,10000000):
    totientNum=totient(n)
    if getKey(n) == getKey(int(totientNum)):
        ratio=float(n)/totientNum
        if minRatio==-1 or ratio < minRatio:
            minRatio=ratio
            result=n

print "Result:",result,minRatio
