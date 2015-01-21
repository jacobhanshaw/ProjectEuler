"""
Current Plan:
1. get primes up to 10,000
2. create set for first prime - dictionary
    [prime]= { candidate numbers }
3. profit (first returned should be smallest)
""" 

import math

# counts[key] = counts.get(key, 0) + 1

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
     

goal=5
maxPrime=10000

primeSets={}

print "Start"

primes=[3,5,7] #skipped 2 on purpose, no prime concatenated with 2 is prime
for i in range(11,maxPrime,2):
    if isPrime(i):
        primes.append(i)

print "Primes done"

for i in range(len(primes)):
    primeSets[primes[i]]=[]
    for j in range(i+1,len(primes)):
        concatA=str(primes[i])+str(primes[j])
        concatB=str(primes[j])+str(primes[i])
        if isPrime(int(concatA)) and isPrime(int(concatB)):
            primeSets[primes[i]].append(primes[j])

print "Sets done"

minSet=[]
minSum=-1

for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        if binarySearchArray(primeSets[primes[i]],primes[j])==-1:
            continue
        intersect=set(primeSets[primes[i]]).intersection(set(primeSets[primes[j]]))
        if 2+len(intersect) < goal:
            continue
        for prime3 in intersect:
            intersect2=intersect.intersection(set(primeSets[prime3]))
            if 3+len(intersect) < goal:
                continue
            for prime4 in intersect2:
                intersect3=intersect2.intersection(set(primeSets[prime4]))
                if len(intersect3) > 0:
                    totalSet=[primes[i],primes[j],prime3,prime4]
                    totalSet.extend(list(intersect3))
                    totalSum=0
                    for num in list(totalSet):
                        totalSum+=num
                    if minSum==-1 or totalSum < minSum:
                        minSum=totalSum
                        minSet=totalSet

print "Set:",minSet,"Sum:",minSum
                                                
print "Done"
