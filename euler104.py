
def isPandigital(numStr):
    numArr=[0] * 10

    for char in numStr:
        numArr[int(char)]+=1

    for i in range(1,10):   #don't care about zero here
        if numArr[i] <> 1:
            return False

    return True

fm2=1
fm1=1
f=2
i=2

tailcut = 1000000000

nums=9

while len(str(f)) < nums*2:  #no need for logic if less than min number given in problem
    i+=1
    f=fm1+fm2
    fm2=fm1
    fm1=f

found = False;
while not found:
    i+=1
    f = (fm1 + fm2) % tailcut
    fm2 = fm1
    fm1 = f
 
    if isPandigital(str(f)):
        t = (i * 0.20898764024997873 - 0.3494850021680094);
        if (isPandigital(str(int(10**(t - int(t) + 8))))):
            found = True;

print "Result:",i
"""
found=False
while not found:
    i+=1
    f = (fm1 + fm2) % tailcut
    fm2 = fm1
    fm1 = f
    
    strF=str(f)
    if isPandigital(strF[:nums]) and isPandigital(strF[len(strF)-nums:]):
        found=True
        print "Result:",i
"""
