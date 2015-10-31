target=7

tens=10
width=1
length=tens-(tens/10)

index=0
number=1
goalPosition=1
currentTens=1
currentPosition=1
difference=0

result=1

while target > 0:
    difference=goalPosition-currentPosition
    while difference > 0:
        rangeValue=length*width
        if difference > rangeValue:
            difference-=rangeValue
            currentTens=tens
            currentPosition+=rangeValue
            difference=goalPosition-currentPosition
            width+=1
            tens*=10
            length=tens-(tens/10)
        else:
            number=currentTens+difference//width
            index=difference % width
            difference=0         
    result*=int((str(number))[index])
    goalPosition*=10
    target-=1

print "Result: ",result
        

    
