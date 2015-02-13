#Add to dict if exists
counts[key] = counts.get(key, 0) + 1

#Read file
baseExpFile = open("base_exp.txt")

for line in baseExpFile:
    nums=line.rstrip().split(",")

#Write file

import os.path

ideasFile =""
namesFile=""

if os.path.isfile("company_ideas.txt"):
    ideasFile = open("company_ideas.txt",'r+')
else:
    ideasFile = open("company_ideas.txt",'w+')

for i in range(len(words)):
    for j in range(len(words[i])):
        ideasFile.write(words[i][j]+"\n")
    ideasFile.write("\n")

ideasFile.close()
namesFile.close()

#Random
from random import randrange

#Permutations
import itertools
x = set(itertools.permutations(str(num)))
pdString="".join(pd)
pdInt=int(pdString)

#Whole Number
.is_integer()
