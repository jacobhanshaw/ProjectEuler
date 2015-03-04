import timeit

def sumOfNumsUpToN(n):
    return n * (n+1) / 2

def sumOfDivByNumUpToMax(num,maxVal):
    n = maxVal // num
    
    return num * sumOfNumsUpToN(n)

def method0(maxVal):
    total = 0
    for x in range (maxVal+1):
        if (x % 3 == 0) or (x % 5 == 0):
            total += x

    return total    

def method1(maxVal):
    return sumOfDivByNumUpToMax(3,maxVal) + sumOfDivByNumUpToMax(5,maxVal) - sumOfDivByNumUpToMax((3*5),maxVal)

execs = 100
maxVal = 999

tm0 = timeit.Timer("method0("+str(maxVal)+")",setup="from __main__ import method0")
tm1 = timeit.Timer("method1("+str(maxVal)+")",setup="from __main__ import method1")

print "Result:",method0(maxVal)
print "Method 0:",min(tm0.repeat(number=execs))/execs
print "Result:",method1(maxVal)
print "Method 1:",min(tm1.repeat(number=execs))/execs

"""
3        (1     
6  . 9   (3
9  . 18  (6
12 . 30  (10
15 . 45  (15
18 . 63  (21
21 . 84  (28
24 . 108 (36
27 . 135 (45
30 . 165 (55
Diff: 2,3,4,5,6,7,8,...
"""
