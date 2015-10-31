power=5

digits=1
maxValue=-1

while maxValue < 0:
    if 9**5*digits<10**digits:
        maxValue=9**5*digits
    digits+=1

result=0
for i in range(2,maxValue,1):
    string=str(i)
    localSum=0
    for j in range(0,len(string),1):
        localSum+=int(string[j])**power
    if localSum==i:
        result+=i

print "Result: ",result
