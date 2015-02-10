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

from math import floor,ceil

def Square(squares,num):
    lenSquares=len(squares)
    if num >= lenSquares:
        for i in range(lenSquares,int(num)+1):
            squares.append(i**2)

    return squares[int(num)]
    
squares=[]

count=0
goalTriangles=1
nonMultSolutions=[]

for num in range(12,1000):#1500001): #start from given min length

    skip=False
    triangles=0

    for modNum in nonMultSolutions:
        if num % modNum == 0:
            triangles+=1
            if triangles > goalTriangles:
                skip=True
                break

    if skip:
        continue

    new=(triangles<=0)

    triangles=0 #Prevent counting twice
    
    c=ceil((num+3)/3.0)
    other=(num-c)/2.0
    while Square(squares,c) < (Square(squares,floor(other))+Square(squares,ceil(other))):
        c+=1
        other=(num-c)/2.0

    skip=False
    while Square(squares,c) <= (Square(squares,(c-1))+Square(squares,(num-c-(c-1)))):
        b=c-1
        a=num-c-b
        cSquared=Square(squares,c)
        while b > a:
            otherSide=(Square(squares,b)+Square(squares,a))
            if cSquared > otherSide:
                break
            if cSquared == otherSide:
                triangles+=1
                if triangles > goalTriangles:
                    skip=True
                break
            b-=1
            a+=1
        if skip:
            break
        c+=1

    if new and triangles > 0:
        nonMultSolutions.append(num)

    if triangles==goalTriangles:
        count+=1

#    print "Num:",num,triangles

print "Result:",count
