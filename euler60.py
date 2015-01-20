"""
Current Plan:
1. get primes up to 10,000
2. store in 2D array [len(num)][index] -can narrow to len then binSearch
    for numbers < 10,000
3. create set for first prime - dictionary
    [prime]= { candidate numbers }
    go through candidate numbers, creating dictionaries if not already created
    upon intersection, see if next set intersects, etc.
4. profit (first returned should be smallest)
""" 

import math

# counts[key] = counts.get(key, 0) + 1

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
