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
    high=len(array)
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

def constructSet(primes,startIndex,primeSets,prime):
    for i in range(startIndex,len(primes)):
        concatA=str(primes[i])+str(prime)
        concatB=str(prime)+str(primes[i])
        if isPrime(int(concatA)) and isPrime(int(concatB)):
            primeSets.get(prime, []).append(primes[i])

def testSet(currentIntersect,startPrime,primeSets,depth,goal):
    newIntersect=currentIntersect.intersection(set(primeSets[startPrime]))
    
    if len(newIntersect) < goal:
        return
        
    depth+=1
    if depth==goal:
        return newIntersect
     
    for prime in newIntersect:
        testSet(newIntersect,prime,primeSets,depth,goal)
     

goal=3
maxPrime=10000

primeSets={}

print "Start"

primes=[3,5,7]
for i in range(11,maxPrime,2):
    if isPrime(i):
        primes.append(i)

print "Primes done"

for i in range(len(primes)):
    primeSets[primes[i]]=[]
    for j in range(len(primes)):
        concatA=str(primes[i])+str(primes[j])
        concatB=str(primes[j])+str(primes[i])
        if isPrime(int(concatA)) and isPrime(int(concatB)):
            primeSets[primes[i]].append(primes[j])

print "Sets done"

for i in range(len(primes)):
    print "Prime: ",primes[i]
    for j in range(i+1,len(primes)):
        result=testSet(set(primeSets[primes[i]]),primes[j],primeSets,0,goal)
        if result:
            print "Result:",result
            total=0
            for num in result:
                total+=num
            print "Total:",total

print "Done"
