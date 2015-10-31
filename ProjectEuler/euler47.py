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

neededFactors=4
neededConsecutive=4

num=1
consecutive=0
while consecutive < neededConsecutive:
    if len(primeFactors(num).items()) == neededFactors:
        consecutive+=1
    else:
        consecutive=0
    num+=1

print "Num:",num-1
print "Result:",(num-4)
