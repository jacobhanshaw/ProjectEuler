from math import sqrt,floor

#initialize to skip the givenvalues up to sqrt(13)

oddCount=4
maxNum=10000

squares=[]
squareIndex=0

num=4
square = num**2
while square <= maxNum:
    squares.append(square)
    num+=1
    square = num**2

for num in range(14,maxNum+1):

#    if num == squares[squareIndex]:
#        squareIndex+=1
#        continue
    
    m=0.0
    d=1.0
    a=float(floor(sqrt(num)))
    savedSqrt=a

    Ms=[]
    Ds=[]
    As=[]

    period=0
    found=False
    while not found:
        m=d*a-m
        d=(num-m**2)/d
        if d == 0:
            print "RAR"
            break
        a = floor((savedSqrt+m)/d)
        for i in range(len(Ms)):
            if m == Ms[i] and d == Ds[i] and a == As[i]:
                period=len(Ms)-i
                break
            
        if period <= 0:
            Ms.append(m)
            Ds.append(d)
            As.append(a)
        else:
            found=True

    if len(Ms) % 2 == 1:
        oddCount +=1

print "Result:",oddCount
