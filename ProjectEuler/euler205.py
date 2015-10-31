
def probabilityOfRoll(numDice,minOnDice,maxOnDice):

    arrayToPopulate = [0] * (numDice*maxOnDice+1)
    f = [minOnDice] * numDice

    while True:
        sumOfDice=0
        for i in range(numDice):
            sumOfDice+=f[i]

        arrayToPopulate[sumOfDice]+=1
        
        i = 0
        while True:
            f[i] += 1
            if f[i] <= maxOnDice:
                break
            f[i] = minOnDice
            i += 1
            if i >= numDice:
                return arrayToPopulate

peterArray=[]
colinArray=[]

peterArray = probabilityOfRoll(9,1,4)
colinArray = probabilityOfRoll(6,1,6)

peterWins = 0
totalPossible = (4**9) * (6**6)

minRoll = 6

#For each possible Colin roll add all possible outcomes that Peter will win
for i in range(minRoll,len(colinArray)):
    for j in range(i+1,len(peterArray)):
        peterWins += colinArray[i] * peterArray[j]

print "Result:",round((float(peterWins)/float(totalPossible)),7)
