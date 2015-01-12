
def nextInNumberChain(num):
    string=str(num)
    result=0
    for i in range(len(string)):
        result += int(string[i])**2

    return result

maxNum=10000000
maxInNumChain=len(str((maxNum-1)))*9**2
cacheSize=maxInNumChain+1
cache = [-1] * cacheSize

result=0
for i in range(1,maxNum):
    num=i
    while num <> 1 and num <> 89:
        num=nextInNumberChain(num)
        if cache[num] <> -1:
            num = 89 if cache[num] == 1 else 1
    if num == 89:
        result+=1
    if i < cacheSize:
        if num == 89:
            cache[i]=1
        else:
            cache[i]=0

print "Result:",result
