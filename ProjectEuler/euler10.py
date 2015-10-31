

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

result=2

for i in range(3,2000000,2):
    if isPrime(i):
        result+=i

print "Result: ",result
