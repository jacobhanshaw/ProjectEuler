

def primeFactors(num):
    results = []

    while num % 2 == 0:
        results.append(2)
        num /= 2
        
    i=3
    maxPos=num

    while i < maxPos:
        
        if num % i == 0:
            results.append(i)
            num /= i
        else:
            maxPos=num/i
            i+=2

    if num > 1:
        results.append(num)

    print results
    


if __name__ == '__main__':
    primeFactors(9) # 600851475143


