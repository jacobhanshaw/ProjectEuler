import math

def triangle(x):
    return (x*(x+1))/2

def hexagon(x):
    return x*(2*x-1)

def isTriangle(x):
    value=math.sqrt(float(8*x+1))
    return value.is_integer() and value % 2 == 1

def isPentagonal(x):
    value=math.sqrt(float(24*x+1))
    return value.is_integer() and value % 6 == 5

def isHexagonal(x):
    value=math.sqrt(float(8*x+1))
    return value.is_integer() and value % 4 == 3

#Hexagonal is odd triangles

for i in range(287,100001,2):
    if isPentagonal(triangle(i)):
        break

print "Result: ",triangle(i)
