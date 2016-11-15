start=999999
maximum=0
startingNum=0
save=0

def Collatz(num):

    terms=1

    while num > 1:
        terms+=1
        if num % 2 == 0:
            num/=2
        else:
            num=3*num+1

    return terms

for i in range(start,0,-1):
    num=Collatz(i)
    if num > maximum:
        maximum=num
        startingNum=i

print "Max: ",startingNum

