
factorials=[1]

for i in range(1,10):
    factorials.append(i*factorials[i-1])

startNum=69
goal=60
result=0

while startNum < 1000000:
    cycle=1
    num=startNum
    prevNum=-1
    while num <> prevNum and num <> 169 and num <> 871 and num <> 872 \
        and num <> 1454 and num <> 45361 and num <> 45362 and num <> 363601:
            strNum=str(num)
            prevNum=num
            num=0
            for char in strNum:
                num+=factorials[int(char)]
            cycle+=1
    if num==169 or num==363601 or num==1454:
        cycle+=2
    elif num==871 or num==872 or num==45361 or num==45362:
        cycle+=1

    if cycle == goal:
        result+=1

    startNum+=1

print "Result:",result
