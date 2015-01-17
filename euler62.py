
def getKey(num):
    numArr=[0] * 10

    for char in str(num):
        numArr[int(char)]+=1

    key=""
    for i in range(10):
        key+=str(numArr[i])

    return key

def getNum(key):
    result=""

    for i in range(len(key)):
        for j in range(int(key[i])):
            result+=str(i)

    return result

goal=5
found=False
current=5
cubeLen=3
counts={}
mins={}
minVal=-1

while not found:
    cube=current**3
    currentLen=len(str(cube))
    if currentLen <> cubeLen:
        cubeLen=currentLen
        for key in counts:
            if counts[key]==goal:
                if minVal==-1 or mins[key] < minVal :
                    minVal=mins[key]
                found=True
        counts={}
        mins={}
    
    key=getKey(cube)
    counts[key] = counts.get(key, 0) + 1
    if mins.get(key,-1)==-1 or cube < mins[key]:
        mins[key]=cube
    current+=1

print "Min: ",minVal
