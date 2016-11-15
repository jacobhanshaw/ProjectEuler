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

def leftRightTruncations(x):
    result=[]
    
    while len(x) > 1:
        x=x[1:]
        result.append(x)
    
    return result

def rightLeftTruncations(x):
    result=[]
    
    while len(x) > 1:
        x=x[:len(x)-1]
        result.append(x)
    
    return result

def testTruncs(truncs):
    for i in range(0,len(truncs),1):
        if not isPrime(int(truncs[i])):
            return False
                       
    return True

primes=11

result=0

for i in range(11,1000001,2):
    if isPrime(i) and testTruncs(leftRightTruncations(str(i))) and testTruncs(rightLeftTruncations(str(i))):
        result+=i
        primes -=1
        if primes == 0:
            break

print "Result: ",result








                           
