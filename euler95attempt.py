import math

def primeFactors(num):

    if num == 0:
        return {}

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
    return (sumOfList((list(allFactors(num))))-num)

def floydCycle(f,x0,maxCycleVal):

    smallest = x0
    tortoise = f(x0)
    hare = f(tortoise)
    while tortoise <> hare:
        if tortoise > maxCycleVal:
            return -1,-1
        hare = f(f(hare))
        tortoise = f(tortoise)
    
    mu = 0
    tortoise = x0
    while tortoise <> hare:
        hare = f(hare)
        tortoise = f(tortoise)
        if tortoise < smallest:
            smallest = tortoise

        mu += 1

    lam = 1
    hare = f(tortoise)
    while tortoise <> hare:
        hare = f(hare)
        lam +=1

    return lam, smallest

maxLen=0
result=0
maxCycleVal=1000000

for i in range(1,10000000,1):
    values = floydCycle(amicable,i,maxCycleVal)
    if values[0] >= maxLen:
        #print "Len:",values[0],values[1]
        maxLen = values[0]
        if values[1] < result:
            result = values[1]

print "Result: ",result

