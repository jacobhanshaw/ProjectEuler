import math

def isPentagonal(x):
    value=math.sqrt(float(24*x+1))
    return value.is_integer() and value % 6 == 5

pentagons=[]
n=1
found=False
while not found:
    current=n*(3*n-1)/2
    pentagons.append(current)
    for i in range(len(pentagons)-2,-1,-1):
        diff=current-pentagons[i]
        aSum=current+pentagons[i]
        if isPentagonal(diff) and isPentagonal(aSum):
            print "Result:",diff
            found=True
            break
    n+=1
