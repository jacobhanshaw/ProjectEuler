maxCycle=0
maxI=0
divLimit=1000 #weakness of this method. Lengthen until no longer reached

for i in range(3,1000,1):
    mod=0
    mods=[]
    loops=0
    startIndex=-1
    remainder=10
    quotient=""
    current=""
    
    while loops < divLimit:
        current=str(remainder//i)
        mod=remainder % i
        if mod==0:
            quotient=""
            break
        mods.append(mod)
        remainder=mod*10
        for j in range(0,len(quotient),1):
            if current == quotient[j] and mod == mods[j]:
                startIndex=j
                break
        if startIndex <> -1:
            break
        quotient+=current
        loops+=1
    if len(quotient) > maxCycle:
        maxCycle=len(quotient)
        maxI=i

print "Result: ",maxI
