from math import floor,sqrt

def isPrime(n):
    if n % 3==0:
        return False
    else:
        r=floor(sqrt(n))
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

    return low-1

goal=50000000
sqrtGoal=int(sqrt(goal))

primes=[2,3,5,7]

num=11
while num <= sqrtGoal:
    if isPrime(num):
        primes.append(num)
    num+=2

squares=[]
maxX=len(primes)
for i in range(maxX):
    squares.append(primes[i]**2)

i=0
cubes=[]
cube = primes[i]**3
while cube < goal:
    cubes.append(primes[i]**3)
    i+=1
    cube = primes[i]**3

i=0
quads=[]
quad = primes[i]**4
while quad < goal:
    quads.append(primes[i]**4)
    i+=1
    quad = primes[i]**4

nums=[]
for quad in quads:
    for cube in cubes:
        quadCube=quad+cube
        for square in squares:
            num=quadCube+square
            if num >= goal:
                break
            nums.append(num)

print "Result:",len(set(nums))
    
"""
\/ Does not consider repeated numbers

i=0
count=0
quad=primes[i]**4
while quad < goal:
    
    numYindex=binarySearchArray(cubes,(goal-quad))
    while numYindex >= 0:

        cube=cubes[numYindex]

        quadPlusCube=quad + cube
        count+=(binarySearchArray(squares,goal-quadPlusCube)+1)

        numYindex-=1

    i+=1       
    quad=primes[i]**4

print "Result:",count
"""

