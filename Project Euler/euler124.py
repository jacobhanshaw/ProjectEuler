from math import sqrt

def primeFactors(num):
    results = []

    added=False
    while num % 2 == 0:
        if not added:
            results.append(2)
        num /= 2
        added=True
        
    i=3
    maxPos=sqrt(num)

    added=False
    while i <= maxPos:
        
        if num % i == 0:
            if not added:
                results.append(i)
            num /= i
            added=True
        else:
            added=False
            i+=2

    if num > 1:
        results.append(num)

    return results

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

nums=[[1]]
rads=[1]
maxNum=100000
for num in range(2,maxNum+1):
    factors = primeFactors(num)
    product = 1
    for factor in factors:
        product *= factor

    if product > rads[len(rads)-1]:
        rads.append(product)
        nums.append([])

    nums[binarySearchArray(rads,product)].append(num)

k=0
index=-1
goal=10000

while k < goal:
    index+=1
    k+=len(nums[index])

size = len(nums[index])
print "Result:",nums[index][(size-(k-goal+1))]
