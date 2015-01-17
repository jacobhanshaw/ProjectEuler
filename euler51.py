import math

def isPrime(n):
    if n % 2==0:
        return False
    elif n % 3==0:
        return False
    else:
        r=math.floor(math.sqrt(n)) # n rounded to the greatest integer r so that r*r<=n
        f=5
        while f<=r:
            if n % f==0:
                return False
            if n % (f+2) == 0:
                return False
            f=f+6

    return True

def findWildCardAnswer(nums,goal):
    numLen = len(str(nums[0]))
    f = [0] * numLen
    while True:
        fittingNums=[]
        for num in nums:
            replaceNum=-1
            fits=True
            stringNum=str(num)
            listNum=list(stringNum)
            for i in range(numLen):
                if f[i]==1:
                    listNum[i]='*'
                    numAtIndex=int(stringNum[i])
                    if replaceNum == -1:
                        replaceNum=numAtIndex
                    elif replaceNum <> numAtIndex:
                        fits=False
                        break
            if fits:
                fittingNums.append("".join(listNum))
        
#        print fittingNums
        streak=0
        currentNum=""
        fittingNums.sort()
        lenFittingNums=len(fittingNums)
        for i in range(lenFittingNums):
            if streak==0:
                currentNum=fittingNums[i]
            if fittingNums[i]==currentNum:
                streak+=1
            else:
                streak=0
            if streak==goal:
                if i+1 < lenFittingNums and fittingNums[i+1] <> currentNum:
                    yield currentNum

        i = 0
        while True:
            f[i] += 1
            if f[i] <= 1:
                break
            f[i] = 0
            i += 1
            if i >= numLen:
                return
goal=8
found=False
minResult=-1

start=10
end=100
while not found:
    primes=[]
    for i in range((start+1),(end+2),2):
        if isPrime(i):
            primes.append(i)
    wildAnswers=list(findWildCardAnswer(primes,goal))
    for wildAnswer in wildAnswers:
        if wildAnswer<>"-1":
            print "Answer:",wildAnswer
            for i in range(10):
                tempList=list(wildAnswer)
                for j in range(len(tempList)):
                    if tempList[j]=='*':
                        tempList[j]=str(i)
                num=int("".join(tempList))
                if isPrime(num) and (minResult==-1 or num < minResult):
                    minResult=num
                    found=True
                    print "Result:",minResult
                    break
        if found:
            break
                
    start*=10
    end*=10
