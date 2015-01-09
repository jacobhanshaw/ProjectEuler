import math

def isPrime(n):
    if n % 3==0:
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

primes=[1,2,3,5,7]

current=9
found=False

while not found:
    if not isPrime(current):
        breaksRule=True
        for i in range(len(primes)-1,-1,-1):
            value=float(current-primes[i])/float(2)
            if value.is_integer() and math.sqrt(value).is_integer():
                    breaksRule=False
                    break
        if breaksRule:
            found=True
            print "Result: ",current
                
    else:
        primes.append(current)
    current+=2
