import os.path
from random import randrange

ideasFile =""
namesFile=""

if os.path.isfile("company_ideas.txt"):
    ideasFile = open("company_ideas.txt",'r+')
else:
    ideasFile = open("company_ideas.txt",'w+')

twoAdjectiveProbability=20
oneAdjectiveProbability=40
nounProbability=80
companyProbability=80

adj=["Super","nTh","Alternative","Divergent","Odd","Augmented","Enhance",\
      "Virtual","Artificial"]
noun=["Transparency","Variant","Clarity","Translucence","Dimension",\
      "Element","Alternative","Divergent","Virtual"]
companyTitle=["Productions","Studios","Games","Inc.","Entertainment"]
words=[adj,noun,companyTitle]

index=0
"""
for line in ideasFile:
    if line == "\n":
        index+=1
    else:
        words[index].append(line.rstrip())
"""
inputLine=""
while inputLine <> "q":
    companyName=""

    indexes=[]

    if randrange(0,100) < twoAdjectiveProbability:
        indexes.append(randrange(0,len(adj)))
        companyName +=adj[indexes[0]]+" "
    else:
        indexes.append(-1)

    if randrange(0,100) < oneAdjectiveProbability:
        indexes.append(randrange(0,len(adj)))
        companyName +=adj[indexes[1]]+" "
    else:
        indexes.append(-1)

    if randrange(0,100) < nounProbability:
        indexes.append(randrange(0,len(noun)))
        companyName +=noun[indexes[2]]+" "
    else:
        indexes.append(-1)

    if randrange(0,100) < companyProbability:
        indexes.append(randrange(0,len(companyTitle)))
        companyName +=companyTitle[indexes[3]]+" "
    else:
        indexes.append(-1)

    inputLine = raw_input(companyName+"\n").lower()

    if len(inputLine) > 0 and (inputLine[0] == "y" or inputLine[0] == "u"):
        for i in range(len(indexes)):
            if indexes[i] > 0:
                temp=words[i][indexes[i]-1]
                words[i][indexes[i]-1]=words[i][indexes[i]]
                words[i][indexes[i]]=temp
                
    if len(inputLine) > 0 and inputLine[0] == "s":
        namesFile.write(companyName+"\n")


for i in range(len(words)):
    for j in range(len(words[i])):
        ideasFile.write(words[i][j]+"\n")
    ideasFile.write("\n")

ideasFile.close()
namesFile.close()
