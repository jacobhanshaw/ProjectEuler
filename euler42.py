import math

def isTriangle(x):
    value=math.sqrt(float(8*x+1))
    return value.is_integer() and value % 2 == 1

wordsFile = open("words.txt")
wordsList = []

for line in wordsFile:
    line=line.replace("\"","")
    wordsList.extend(line.split(","))

result=0
for i in range(0,len(wordsList),1):
    
    word=wordsList[i].lower()
    wordValue=0
    for j in range(0,len(word),1):
        wordValue+=ord(word[j])-96

    if isTriangle(wordValue):
        result+=1

print "Result: ",result
    
