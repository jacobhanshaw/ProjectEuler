
count=0
num=100

goal=0.99
found=False

while not found:
    
    strNum=str(num)
    bCount=count
    direction=0
    for i in range(len(strNum)-1):
        if strNum[i] < strNum[i+1]:
            if direction == 0:
                direction=1
            elif direction!=1:
                count+=1
                break
        if strNum[i] > strNum[i+1]:
            if direction == 0:
                direction=-1
            elif direction!=-1:
                count+=1
                break
            
    if float(count)/float(num) == goal:
        print "Num:",num
        found=True

    num+=1
    
