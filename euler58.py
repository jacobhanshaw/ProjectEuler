
import math

def isPrime(n):
    if n % 2 == 0:
        return False
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


primes=3
totalDiagonal=5

last=9
sideLengthLessOne=2

desiredPercentage=0.1

while float(primes)/float(totalDiagonal) >= desiredPercentage:
    sideLengthLessOne+=2
    for i in range(4):
        last+=sideLengthLessOne
        if isPrime(last):
            primes+=1
        totalDiagonal+=1

print "Result: ",(sideLengthLessOne+1)
