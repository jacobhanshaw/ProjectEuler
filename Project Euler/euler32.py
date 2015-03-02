"""
Possible: (in digits)
1 * 4 = 4
2 * 3 = 4

Not Possible:
1 * 3 = 4 ( 8 possible)
1 * 5 = 5 (11 possible)
2 * 2 = 4 ( 8 possible)
2 * 4 = 5 (11 possible)
3 * 3 = 5 (11 possible)
"""

def testPanDigital(num,used):
    numStr=str(num)
    for i in range(0,len(numStr)):
        index=int(numStr[i])-1
        if index < 0 or used[index]:
            return False
        else:
            used[index]=True

    return True

products=[]

for i in range(2,10):
    digitUsedOuter = [False] * 9
    digitUsedOuter[i-1]=True
    for j in range(1234,5000): #non-zero/repeating start-10000/2
        product=i*j
        if product > 10000:
            break

        digitUsed=list(digitUsedOuter)
        
        if testPanDigital(j,digitUsed) and testPanDigital(product,digitUsed):
            products.append(product)

for i in range(12,100):
    digitUsedOuter = [False] * 9
    if not testPanDigital(i,digitUsedOuter):
        continue
    for j in range(123,834): #non-zero/repeating start-10000/12
        product=i*j
        if product > 10000:
            break

        digitUsed=list(digitUsedOuter)
        
        if testPanDigital(j,digitUsed) and testPanDigital(product,digitUsed):
            products.append(product)

products=set(products)

result=0
for product in products:
    result+=product
    
print "Result: ",result
