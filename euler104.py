
def isPandigital(numStr):
    numArr=[0] * 10

    for char in numStr:
        numArr[int(char)]+=1

    for i in range(10):
        if numArr[i] <> 1:
            return False

    return True

fm2=1
fm1=1
f=2
i=3
nums=9

while len(str(f)) < nums*2:
    fm2=fm1
    fm1=f
    f=fm1+fm2
    i+=1
    
print "Long Enough"

found=False
while not found:
    fm2=fm1
    fm1=f
    f=fm1+fm2
    i+=1
    
    strF=str(f)
    if isPandigital(strF[:nums]) and isPandigital(strF[len(strF)-nums:]):
        found=True
        print "Result:",i
      
