from math import floor,sqrt

#Start off with given info
#x^2-1=d*y^2
#y^2=(x^2-1)/d

result=5
maxMinX=9
maxN=1000


squares=[]
num=2
square=num**2
while square <=maxN:
    squares.append(square)
    num+=1
    square=num**2

squares.append(square) #Adding extra value to prevent out of bounds exception

squareIndex=0
for D in range(2,maxN+1):

    if D == squares[squareIndex]:
        squareIndex+=1
        continue

    m=0
    d=1
    a=int(floor(sqrt(D)))
    savedSqrt=a

    numm1=1
    num=a

    otherDm1=0
    otherD=1
    
    while (num**2 - D*(otherD**2)) <> 1:
        m=d*a-m
        d=(D-m**2)//d
        a = (savedSqrt+m)//d
            
        numm2=numm1
        numm1=num

        otherDm2=otherDm1
        otherDm1=otherD

        num = a*numm1+numm2
        otherD=a*otherDm1+otherDm2
    
    if num > maxMinX:
        maxMinX=num
        result=D

print "Result:",result
