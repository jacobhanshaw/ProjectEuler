import time

def factorial(top,limit):
    result=1
    for i in range(top,limit,-1):
        result*=i
    return result

def binomialCoefficient(n,k):
    return factorial(n,k)/factorial(k,1)

"""
0111111
1234
136
14
15
16
"""

squareSize=20

print "Array: "
t0 = time.time()
array2D=[[0 for x in range(squareSize+1)] for x in range(squareSize+1)]

for i in range(0,squareSize+1,1):
    for j in range(0,squareSize+1,1):
        if i == 0 or j == 0:
            array2D[i][j]=1
        else:
            array2D[i][j]=array2D[i-1][j]+array2D[i][j-1]

print "Result: ",array2D[i][j]
t1 = time.time()

print "Time: ",(t1-t0)

print ""

print "Binomial Coefficient: "
t0 = time.time()
print "Result: ",binomialCoefficient((squareSize*2),squareSize)
t1 = time.time()

print "Time: ",(t1-t0)

