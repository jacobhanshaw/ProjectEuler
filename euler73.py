from math import ceil
from fractions import gcd

lowFraction=(1.0/3.0)
highFraction=0.5

count=3
closestFraction=-1


for i in range(9,12001):
    numerator=lowFraction * i
    if numerator.is_integer():
        numerator+=1
    else:
        numerator=ceil(numerator)
    currentFraction=numerator/float(i) 
    while currentFraction < highFraction:
        if gcd(numerator,i) == 1:
            count+=1
        numerator+=1
        currentFraction=numerator/float(i) 

print "Result:",count
    
