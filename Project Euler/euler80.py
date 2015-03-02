import decimal

def binarySearchArray(array,goal):
    low=0
    high=len(array)-1
    while low<=high:
        mid=(high+low)//2
        current=array[mid]
        if goal < current:
            high=mid-1
        elif goal > current:
            low=mid+1
        else:
            return mid

    return low-1

maxNum=100
numDecimalPlaces=100
extraPlaces=2

squares=[]
num=1
square=num**2
while square <=maxNum:
    squares.append(square)
    num+=1
    square=num**2

squares.append(square) #Adding extra value to prevent out of bounds exception

last=0
total=0
start=2
squareIndex=0
precision = decimal.Context(prec=(numDecimalPlaces+extraPlaces))
for num in range(1,maxNum+1):
    last=total
    if num == squares[squareIndex]:
        squareIndex+=1
        continue
    
    d = decimal.Decimal(num)
    strD=str(d.sqrt(precision))

    for char in strD[:len(strD)-extraPlaces]:
        if char <> '.':
            total+=int(char)
        

print "Result:",total
