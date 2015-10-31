import sys 
#import os
#sys.path.append(os.path.abspath("../Algorithms/"))

#import ESieve

def generateFactors(limit):
  sumOfFactorsList = [0] * (limit+1)
  for i in range(1,int(limit/2 + 1)):
    for j in range(i*2, (limit+1), i):
      sumOfFactorsList[j] += i

  return sumOfFactorsList

def sieve():
  result = 0
  limit = 1000000
  chainLength = 0

  factors = generateFactors(limit)
  numbers = [False] * (limit + 1)

  for i in range(2, (limit+1)):
    if numbers[i]:
      continue

    chain = []
    newNumber = i
    broken = False

    while newNumber not in chain:
      chain.append(newNumber)
      newNumber = factors[newNumber]

      if(newNumber > limit or numbers[newNumber]):
        broken = True
        break

    if not broken:
      smallest = sys.maxint
      first = chain.index(newNumber)

      if(len(chain) - first > chainLength):
        for j in range(first, len(chain)):
          if chain[j] < smallest:
            smallest = chain[j]

        chainLength = len(chain) - first
        result = smallest

    for j in range(0, len(chain)):
      numbers[chain[j]] = True

  print "Result: ", result

sieve()
