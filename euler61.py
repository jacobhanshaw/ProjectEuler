from math import sqrt,floor,ceil
import copy

"""
It can be noted that all these term n of each of these is
P(n-1) greater than the one beneath it.

Hexagonal is odd triangles

For example,
Square(n)=Triangle(n)+Triangle(n-1)
Pentagonal(n)=Square(n)+Triangle(n-1)
etc.
"""

def triangle(x):
    return (x*(x+1))/2

def getNFromTriangle(x):
    return (sqrt(float(8*x+1))-1)/2

def square(x):
    return x**2

def getNFromSquare(x):
    return sqrt(x)

def pentagonal(x):
    return (x*(3*x-1))/2

def getNFromPentagonal(x):
    return (sqrt(float(24*x+1))+1)/6

def hexagonal(x):
    return x*(2*x-1)

def getNFromHexagonal(x):
    return (sqrt(float(8*x+1))+1)/4

def heptagonal(x):
    return (x*(5*x-3))/2

def getNFromHeptagonal(x):
    return (sqrt(float(40*x+9))+3)/10

def octagonal(x):
    return x*(3*x-2)

def getNFromOctagonal(x):
    return (sqrt(float(12*x+4))+2)/6


def getCyclicalNums(nums,skipList,depth,goal,key,startKey,result):

    for i in range(len(nums)):
        if i in skipList:
            continue
        if not key in nums[i].keys():
            return False

        newList=copy.copy(skipList)
        newList.append(i)
        
        for val in nums[i][key]:
            if val in result:
                continue
            result.append(val)
            nextKey=str(val)[keyLen:]
            if depth==goal and nextKey==startKey:
                return True
            if not getCyclicalNums(nums,newList,depth+1,goal,nextKey,startKey,result):
                result.pop()
            else:
                return True
        


minVal=1000
maxVal=9999

keyLen=2
totalLen=4
restLen=totalLen-keyLen

triangles={}
squares={}
pentagonals={}
hexagonals={}
heptagonals={}
octagonals={}

num=[triangle,square,pentagonal,hexagonal,heptagonal,octagonal]
getN=[getNFromTriangle,getNFromSquare,getNFromPentagonal,getNFromHexagonal,getNFromHeptagonal,getNFromOctagonal]
nums=[triangles,squares,pentagonals,hexagonals,heptagonals,octagonals]
goalDepth=len(num)-1
"""
num=[triangle,square,pentagonal]
getN=[getNFromTriangle,getNFromSquare,getNFromPentagonal]
nums=[triangles,squares,pentagonals]
goalDepth=2
"""

for i in range(len(nums)):
    lowN=int(ceil(getN[i](minVal)))
    highN=int(floor(getN[i](maxVal)))
    for n in range(lowN,highN+1):
        val=num[i](n)
        strVal=str(val)
        key=strVal[:keyLen]
        nums[i].setdefault(key,[])
        nums[i][key].append(val)

result=[]
found=False
skipList=[0]
for key in nums[0].keys():
    for val in nums[0][key]:
        result.append(val)
        nextKey=str(val)[keyLen:]
        found=getCyclicalNums(nums,skipList,1,goalDepth,nextKey,key,result)
        if found:
            break
        result.pop()
    if found:
        break

print "Set:",result

total=0
for value in result:
    total+=value

print "Sum:",total
