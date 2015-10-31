import math
import itertools

def isPrime(n):
    """
    if n==1:
        return False
    elif n<4:
        return True
    elif n % 2 == 0:
        return False
    elif n<9:
        return True
    """
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

def isPanDigital(num):
    used = [False] * 9
    numStr=str(num)
    for i in range(0,len(numStr)):
        index=int(numStr[i])-1
        if index < 0 or used[index]:
            return False
        else:
            used[index]=True

    return True

string="1"

for i in range(2,10):
    string+=str(i)
    x = list(itertools.permutations(string))
    for j in range(len(x)-1,-1,-1):
        value = int("".join(x[j]))
        if isPrime(value):
            print "Result: ",value
            break
