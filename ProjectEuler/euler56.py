
def digitalSum(num):
    total=0
    strNum=str(num)
    for i in range(len(strNum)):
        total+=int(strNum[i])

    return total

maxValue=100

maxSum=0

for a in range(maxValue+1,2,-1):
    if a % 10 == 0:
        continue
    for b in range(maxValue+1,2,-1):
        product=a**b
        tempSum=digitalSum(product)
        if tempSum > maxSum:
            maxSum=tempSum
        if tempSum < maxSum/2:
            break

print "Result:",maxSum
