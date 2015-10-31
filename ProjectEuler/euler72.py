from math import sqrt

#Need to read up on other solutions and come back to this

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
            
    return int(result)

count=0
for num in range(2,1000001):
    count+=totient(num)

print "Result:",count
