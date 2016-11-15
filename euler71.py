from math import floor 

goalFraction=(3.0/7.0)

closestFraction=-1
rNum=-1
rDenom=-1

for i in range(8,1000001,1):
    numerator=floor(goalFraction * i)
    currentFraction=numerator/float(i) 
    if (numerator % 3 <> 0 or i % 7 <> 0) and currentFraction >= closestFraction:
        rNum=numerator
        closestFraction=currentFraction

print "Result:",int(rNum)
    
