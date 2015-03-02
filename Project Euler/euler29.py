combList=[]

for i in range(2,101,1):
    for j in range(2,101,1):
        combList.append(i**j)

print "Result: ",len(list(set(combList)))
