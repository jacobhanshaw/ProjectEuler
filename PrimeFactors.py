import time
import math

def primeFactors(num):

    factors={}
    startNum=num

    while num % 2 == 0:
        factors[2]=factors.get(2,0)+1
        num /= 2
        
    i=3
    maxPos=math.sqrt(num)

    while i <= maxPos:
        
        if num % i == 0:
            factors[i]=factors.get(i,0)+1
            num /= i
        else:
            i+=2

    if num > 1 and num <> startNum:
        factors[num]=factors.get(num,0)+1

    return factors

def primeFactorsA(num):

    factors={}
    startNum=num

    while num % 2 == 0:
        factors[2]=factors.get(2,0)+1
        num /= 2
        
    i=3
    maxPos=num

    while i < maxPos:
        
        if num % i == 0:
            factors[i]=factors.get(i,0)+1
            num /= i
        else:
            i+=2
            maxPos=num/i

    if num > 1 and num <> startNum:
        factors[num]=factors.get(num,0)+1

    return factors




testNum=9
t0 = time.time()
print primeFactorsA(testNum)
t1 = time.time()
print "Time: ",(t1-t0)

t0 = time.time()
print primeFactors(testNum)
t1 = time.time()
print "Time: ",(t1-t0)
