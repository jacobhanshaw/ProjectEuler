import math

digits=1
maxValue=-1

factorials=[]

for i in range(0,10,1):
    factorials.append(math.factorial(i))

while maxValue < 0:
    value=factorials[9]*digits
    if value<10**digits:
        maxValue=value
    digits+=1

result=0

for i in range(3,maxValue,1):
    string=str(i)
    localSum=0
    for j in range(0,len(string),1):
        localSum+=factorials[int(string[j])]
    if localSum==i:
        result+=i

print "Result: ",result

