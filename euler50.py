import math

def isPrime(n):
    if n==1:
        return False
    elif n<4:
        return True
    elif n % 2 == 0:
        return False
    elif n<9:
        return True
    elif n % 3==0:
        return False
    else:
        r=math.floor(math.sqrt(n)) # n rounded to the greatest integer r so that r*r<=n
        f=5
        while f<=r:
            if n % f==0:
                return False
            if n % (f+2) == 0:
                return False
            f=f+6

    return True

maxSize=1000000

num=3
total=2

result=2
maxLength=1

primes=[]
primes.append(2)

while len(primes) >= maxLength:
    
    if isPrime(num):
        total+=num
        primes.append(num)
        
    while total >= maxSize:        
        remove=primes.pop(0)
        total-=remove
    
    length=len(primes)
    localTotal=total
    removeIndex=0
    while (not isPrime(localTotal)) and length > maxLength:
        localTotal-=primes[removeIndex]
        removeIndex+=1
        length-=1
        
    if length > maxLength and isPrime(localTotal):
        result=localTotal
        maxLength=length
    
    num+=2

print "Result: ",result
