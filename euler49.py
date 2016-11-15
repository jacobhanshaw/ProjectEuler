import math
import itertools

#weak sauce. Wanted guaranteeed Friday commit. (Late Thursday night.)

def isPrime(n):
    if n % 2 == 0:
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


num=1001
test=[]
result=[]
permutations=[]

resultLength=12
numResultTerms=3

found=False
while not found:
    if isPrime(num):
        permutations=[]
        x = set(itertools.permutations(str(num)))
        for pd in x:
            pdString="".join(pd)
            pdInt=int(pdString)
            if num <> pdInt and pdInt > 1000 and isPrime(pdInt):
                permutations.append(pdInt)
        permutations.sort()
        for i in range(len(permutations)-1,-1,-1):
            if permutations[i] == 8147:
                break
            for j in range(i-1,-1,-1):
                difference=(permutations[i]-permutations[j])
                for k in range(j-1,-1,-1):
                    differenceTwo=(permutations[j]-permutations[k])
                    if difference<differenceTwo:
                        break
                    elif difference==differenceTwo:
                        result.append(permutations[k])
                        result.append(permutations[j])
                        result.append(permutations[i])
                        found=True
                        break
            if found:
                break
        if found:
            break
    num+=2

print "Result:",result[0],result[1],result[2]
