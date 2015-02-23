#3 cycle - 202326
#4 cycle - 
"""
def halfCycle(array):

    lenArray = len(array)
    if lenArray < 4 or lenArray % 2 == 1:
        return False

    strArray="".join(map(str,array))

    cycleLength = len(strArray)/2

    if strArray[:cycleLength] == strArray[cycleLength:]:
        return True

    return False

addSquares=[9,27,81]
current=[4,8,16]
subSquares=[]

rMaxTotal=0

for num in range(3,1001):
    print num
    subSquares=current
    current = addSquares
    currentSquared = current[0]
    addSquares=[]

    zeros=0
    rMax=0
    power=2
    subIndex=0
    rSoFar=[]
    while not halfCycle(rSoFar):

        if subIndex >= len(subSquares):
            subSquares.append((num-1)**power)
            
        lessOne=subSquares[subIndex]
        plusOne=(num+1)**power
        addSquares.append(plusOne)

        r = (lessOne + plusOne) % currentSquared

        rSoFar.append(r)

        if r > rMax:
            rMax = r

        subIndex+=1
        power+=1

    rMaxTotal+=rMax
    
"""
rMaxTotal = 0
for num in range(3,1001):
    rMaxTotal += 2 * num * ((num-1) / 2)

print "Result:",rMaxTotal


