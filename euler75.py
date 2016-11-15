"""
Knowledge:
c > b > a
Proof:
c > b and c > a
as c^2 = b^2+a^2 where a,b,c are positive non-zero integers
b > a
As if a==b
a^2+a^2 would = (sqrt(2) * a)^2
An irrational number (sqrt(2)) multiplied a rational number (a) is irrational,
so (a * sqrt(2))=c would be irrational and c must be rational

Since c > b > a
Min c can be found as follows:
perimeter = c+b+a
perimeter = x+(x-1)+(x-2)
ceil((perimeter+3)/3)=x
"""

import numpy as np

def getTriplets(triangle,A,B,C,perimeters,maxVal):
    perimeter=triangle[0]+triangle[1]+triangle[2]
    if perimeter <= maxVal:
        perimeters.append(perimeter)
        getTriplets(A*triangle,A,B,C,perimeters,maxVal)
        getTriplets(B*triangle,A,B,C,perimeters,maxVal)
        getTriplets(C*triangle,A,B,C,perimeters,maxVal)
    

goalTriangles=1

maxVal=1500000
counts=[0]*(maxVal+1)
perimeters=[]

A = np.matrix( [[ 1,-2, 2], [ 2,-1, 2], [ 2,-2, 3]] )
B = np.matrix( [[ 1, 2, 2], [ 2, 1, 2], [ 2, 2, 3]] )
C = np.matrix( [[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]] )

triangle=np.matrix( [[3],[4],[5]] )

getTriplets(triangle,A,B,C,perimeters,maxVal)

for num in perimeters:
    for mult in range(num,maxVal+1,num):
        counts[mult]+=1

count=0
for numTriangles in counts:
    if numTriangles == goalTriangles:
        count+=1

print "Result:",count
