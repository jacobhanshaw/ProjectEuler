

namesFile = open("names.txt")
namesList = []

for line in namesFile:
    line=line.replace("\"","")
    namesList.extend(line.split(","))

namesList.sort()

result=0
for i in range(0,len(namesList),1):
    name=namesList[i].lower()
    nameValue=0
    for j in range(0,len(name),1):
        nameValue+=ord(name[j])-96
    
    result+=nameValue*(i+1)

print "Result: ",result

