import math

def rotation(string):
    return string[1:] + string[0]

def rotations(string,rList):
    current=rotation(string)
    while current<>string:
        rList.append(current)
        current=rotation(current)

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

result=13 #know primes under 100 that are circular, simplifies isPrime

for i in range(101,1000001,2):
    if not isPrime(i):
        continue
    string=str(i)
    rList=[]
    rotations(string,rList)

    allPrime=True
    for j in range(0,len(rList),1):
        if not isPrime(int(rList[j])):
            allPrime=False
            break
    if allPrime:
        result+=1

print "Result: ",result

