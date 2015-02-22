
from fractions import gcd

maxX = 50
maxY = 50

total = maxX * maxY * 3 #Account for right angles on axes

#For all other slopes
for x in range(1,(maxX+1)):
    for y in range(1,(maxY+1)):
        greatestFactor = gcd(x,y)
        total += min(y*greatestFactor/x, (maxX - x)*greatestFactor/y)*2

print "Result:",total
