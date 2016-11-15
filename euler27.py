import math

def isPrime(n):
    if n<=1:
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

def test(a,b):
    result=1
    n=1
    quad=0
    while True:
        quad=n**2+a*n+b
        if isPrime(quad):
            result+=1
            n+=1
        else:
            return result

testResult=0
maxPrimes=40 #a max given in problem
bestA=-1
bestB=-1

test(-999,61)

#Test +/- 2
for a in range(-1000,1001,1):
    testResult=test(a,2)
    if testResult > maxPrimes:
        bestA=a
        bestB=2
        maxPrimes=testResult
    testResult=test(a,-2)
    if testResult > maxPrimes:
        bestA=a
        bestB=-2
        maxPrimes=testResult

for b in range(3,1001,2):
    if not isPrime(b):
        continue
    for a in range(-1000,1001,1):
        testResult=test(a,b)
        if testResult > maxPrimes:
            bestA=a
            bestB=b
            maxPrimes=testResult
        testResult=test(a,-b) 
        if testResult > maxPrimes:
            bestA=a
            bestB=-b
            maxPrimes=testResult

print "Max: ",maxPrimes," A: ",bestA," B: ",bestB," Solution: ",(bestA * bestB)
