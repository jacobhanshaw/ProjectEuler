from math import floor,ceil,sqrt

"""
12:
7+5
7+3+2
5+5+2
3+3+3+3
3+3+2+2+2
2+2+2+2+2+2

15:
7+5+3
7+3+3+2
7+2+2+2+2
5+5+5
5+5+3+2
5+3+3+2+2
3+3+3+2+2+2
3+3+3+3+3
3+2+2+2+2+2+2
"""

def binarySearchArray(array,goal):
    low=0
    high=len(array)-1
    while low<=high:
        mid=(high+low)//2
        current=array[mid]
        if goal < current:
            high=mid-1
        elif goal > current:
            low=mid+1
        else:
            return mid

    return -1

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
maxGuess=1000

c=[0]*(5000+1)
c[0]=1

primes=[2,3,5,7]

num=11
while num < maxGuess:
    if isPrime(num):
        primes.append(num)
    num+=2

for k in primes:
    for i in range(0,goal-k+1,1):
        c[i+k]+=c[i]

i=0
while c[i] < goal:
    i+=1

print "I:",i
print c[i-1],c[i],c[i+1]

optionsStart=2
options=[1,1,1,2,2,3,2,1,3]

"""
num=10
found=False
while not found:

    count=0

    for i in range(int(ceil(num/2)),num):
        oneNum=i
        otherNum=num-i
        if isPrime(oneNum) and isPrime(otherNum):
            count+=options[oneNum-optionsStart]
            count+=options[otherNum-optionsStart]
            break
        
    if isPrime(num):
        primes.append(num)
        count+=1
    elif num % 2 == 0:
        count+=1

    if count > goal:
        print "Result:",num
        break
    
    options.append(count)
    num+=1
"""
