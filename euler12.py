
goalDivisors=500

def totalFactors(num):

    result=1

    currFactors=0

    while num % 2 == 0:
        currFactors+=1
        num /= 2

    result*=(currFactors+1)
        
    i=3
    maxPos=num
    currFactors=0

    while i < maxPos:
        
        if num % i == 0:
            currFactors+=1
            num /= i
        else:
            if currFactors > 0:
                result*=(currFactors+1)
                currFactors=0
            maxPos=num/i
            i+=2

    if num > 1:
        result*=2

    return result

def GaussianSum(n):
    return (n * (n+1))/2

def numDivisors(num):
    result=2
    
    for i in range(2,num,1):
        if num % i == 0:
            result+=1
            
    return result

n=500
addNum=n+1
total=GaussianSum(n)
found=False

while not found:
    total+=addNum
    if totalFactors(total) > goalDivisors:
        print "Result: ",total
        found = True
    addNum+=1
