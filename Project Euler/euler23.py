import math

def primeFactors(num):
#    if num == 0:
#        return {}
    
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
#    if num == 0:
#        return 0
    
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

def abundant(num):
    return (sumOfList((list(allFactors(num))))-num) > num


result=0
abundantList=[]
for i in range(1,28124,1):
    if abundant(i):
        abundantList.append(i)

for i in range(1,28124,1):
    index=0
    found=False
    while abundantList[index] < i:
        if abundant(i-abundantList[index]):
            found=True
            break
        index+=1
    if not found:
        result+=i
      

print "Result: ",result

