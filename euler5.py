minFactor=2
maxFactor=20

def primeFactors(num,results):
    gen = ((i, 0) for i in range(minFactor, maxFactor, 1))
    factors=dict(gen)

    while num % 2 == 0:
        factors[2]+=1
        num /= 2
        
    i=3
    maxPos=num

    while i < maxPos:
        
        if num % i == 0:
            factors[i]+=1
            num /= i
        else:
            maxPos=num/i
            i+=2

    if num > 1:
        print "Num: ",num
        factors[num]+=1

    print factors

    return factors


if __name__ == '__main__':
    gen = ((i, 0) for i in range(minFactor, maxFactor, 1))
    results=dict(gen)
    for i in range(2,20,1):
        factors = primeFactors(i,results) # 600851475143
        for j in range(minFactor, maxFactor, 1):
            if factors[j] > results[j]:
                results[j] = factors[j]

    print results

    result=1

    for i in range(minFactor,maxFactor,1):
        print i
        for j in range(0, results[i], 1):
            print "Happens with i: ",i
            result *= i

    print "Final Result: ",result


'''
num = 20
found = False

while not found:

    for i in range(20,11,-1):
        if num % i != 0:
            break

        if i == 11:
            found = True

    num +=20

    print "Num: ",num

print num
'''
