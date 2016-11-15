from math import floor,sqrt

def isPrime(n):
    if n % 3==0:
        return False
    else:
        r=floor(sqrt(n)) # n rounded to the greatest integer r so that r*r<=n
        f=5
        while f<=r:
            if n % f==0:
                return False
            if n % (f+2) == 0:
                return False
            f=f+6

    return True

goal=5000
maxGuess=100

c=[0]*(maxGuess+1)
c[0]=1

primes=[2,3,5,7]

num=11
while num < maxGuess:
    if isPrime(num):
        primes.append(num)
    num+=2

for k in primes:
    for i in range(0,maxGuess-k+1,1):
        c[i+k]+=c[i]

i=0
while c[i] <= goal:
    i+=1

print "Result:",i
