englishWords = { 1: ["a","i"],
                  2: ["be","to","of","in","it","on","he","as",
                "do","at","by","we","or","an","my","so","up","if","go","me"],
                 3:["the","and","for","not","you","but","his","say",
                    "her","she","one","all","out","who","get"],
                 4:["that","have","with","this","from","they","will","what"],
                 5:["would","there","their","about","which"] }

def checkForWord(word):
    
    for commonWord in englishWords[len(word)]:
        if word == commonWord:
            return True

    return False

lettersFile = open("cipher.txt")
lettersList = []

for line in lettersFile:
    lettersList.extend(line.split(","))

probability=0
necessaryProbability=10


#Section to see the result:
"""
result=""

for i in range(0,len(lettersList),1):
    nextLetter=int(lettersList[i])
    
    if i % 3 == 0:
        nextLetter^=103
    elif i % 3 == 1:
        nextLetter^=111
    elif i % 3 == 2:
        nextLetter^=100
        
    result+=str(unichr(nextLetter))

print "Password:",(str(unichr(103))+str(unichr(111))+str(unichr(100)))
print "Result:",result

"""
for password0 in range(ord('a'),ord('z')+1):
   for password1 in range(ord('a'),ord('z')+1):
        for password2 in range(ord('a'),ord('z')+1):
            currentWord=""
            probability=0
            sumOfValues=0
            for i in range(0,len(lettersList),1):
                nextLetter=int(lettersList[i])
                if i % 3 == 0:
                    nextLetter^=password0
                elif i % 3 == 1:
                    nextLetter^=password1
                elif i % 3 == 2:
                    nextLetter^=password2
                sumOfValues+=nextLetter
                if nextLetter < 32: #Rarely used characters below space
                    probability-=1
                if nextLetter == ord(' '):
                    if len(currentWord) > 5 or len(currentWord) < 1:
                        probability-=len(currentWord)//5
                    elif checkForWord(currentWord):
                        probability+=len(currentWord)
                    currentWord=""
                else:
                    currentWord+=str(unichr(nextLetter))
                if probability < -necessaryProbability:
                    break
            if probability > necessaryProbability:
                print "Password:",password0,password1,password2
                print "Sum:",sumOfValues

print "END"

