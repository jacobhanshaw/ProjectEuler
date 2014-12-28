index=2

num=1
lastNum=1
strNum=str(num)
while(len(str(num))<1000):
    temp=num
    num+=lastNum
    lastNum=temp
    index+=1

print "Num: ",index


