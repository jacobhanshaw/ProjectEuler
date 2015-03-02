from math import sqrt,floor,ceil

goal=0.5
start=1000000000000
lastNum=start-1
current=start*(lastNum)

fraction=0.0
numeratorOne=0

"""
while fraction <> goal:
    numeratorOne = sqrt((current/float(2)))
    if not numeratorOne.is_integer():
        numerator = ceil(numeratorOne)*floor(numeratorOne)
        fraction = numerator/float(current)
    lastNum+=1
    current += (lastNum*2)

print "Result:",int(ceil(numeratorOne)),lastNum
"""

#Given values
blue = 85
total = 120
goal = 10**12
while total <= goal:
    blue,total = 3*blue + 2*total -2,4*blue + 3*total - 3

print "Result:",blue
print "Total:",total
