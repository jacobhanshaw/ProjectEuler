
goalPrime=10001

currentNum=15
currentPrime=6


def isPrime(num):

    if num % 2 == 0:
        return False
        
    i=3
    maxPos=num

    while i < maxPos:
        
        if num % i == 0:
            return False
        else:
            maxPos=num/i
            i+=2

    return True

while currentPrime<goalPrime:
    if isPrime(currentNum):
        currentPrime+=1

    currentNum+=2

print "Result: ",currentNum-2
