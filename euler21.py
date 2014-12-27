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

def allFactors(num):
    factors = primeFactors(num).items()
    nfactors = len(factors)
    if nfactors < 1:
        yield 1
        yield num
        return
    
    f = [0] * nfactors

    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return
            
def sumOfList(numList):
    sumList=0
    for i in range(len(numList)):
        sumList+=numList[i]
    return sumList

def amicable(num):
    sumFactors=sumOfList((list(allFactors(num))))-num
    if sumFactors==num:
        return False
    sumOfSumFactors=(sumOfList((list(allFactors(sumFactors))))-sumFactors)
    if num==sumOfSumFactors:
        return True

    return False

result=0
for i in range(1,10000,1):
    if amicable(i):
        result+=i

print "Result: ",result

