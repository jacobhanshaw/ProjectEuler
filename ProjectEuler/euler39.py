import math
from fractions import gcd

result=0
maxCount=0
"""
for i in range(1,1001):
    count=0
    s2 = i // 2
    mlimit = math.sqrt(s2)-1
    for m in range(2,int(math.ceil(mlimit))):
        if s2 % m == 0:
            sm = s2 // m
            while sm % 2 == 0:
                sm = sm // 2
            if m % 2 == 1:
                k = m+2
            else:
                k = m+1
            while k < 2*m and k <= sm:
                if sm % k == 0 and gcd(k,m) == 1:
                    
                    d = s2 // (k*m)
                    n = k-m
                    a = d*(m*m-n*n)
                    b = 2*d*m*n
                    c = d*(m*m+n*n)
                    
                    count+=1
            

                k += 2

    if count > maxCount:
        maxCount=count
        result=i

print "Result: ",i

"""
power=2

for goalSum in range(1,1000,1):

    count=0
    goalSquare=0

    for c in range(goalSum-2,0,-1):
        goalSquare=c**power
    
        for b in range(goalSum-c-1,0,-1):
    
            a=goalSum-c-b

            if (a**power + b**power)==goalSquare:
                count+=1
                
    if count > maxCount:
        maxCount=count
        result=goalSum

print "Result: ",result

