number = 2**1000
print "Number: ",number

numberString=str(number)

result=0

for i in range(0,len(numberString),1):
    result+=int(numberString[i])

print "Result: ",result
