
def setUsed(num,used):
    numStr=str(num)
    for i in range(0,len(numStr)):
        index=int(numStr[i])-1
        used[index]+=1

#Trade-off copy array time vs. potential to break early if subtracting from original
def matchingUsed(num,used):
    local= [0] * len(used)
    numStr=str(num)
    for i in range(0,len(numStr)):
        index=int(numStr[i])-1
        local[index]+=1

    for i in range(0,len(local)):
        if local[i] <> used[i]:
            return False

    return True

result=1
found=False
while not found:
    used=[0] * 9
    setUsed(result,used)
    if result == 142858:
        print "Used: ",used
    if matchingUsed(2*result,used) and matchingUsed(3*result,used) and matchingUsed(4*result,used) and matchingUsed(5*result,used) and matchingUsed(6*result,used):
        found=True
    else:
        result+=1

print "Result: ",result
