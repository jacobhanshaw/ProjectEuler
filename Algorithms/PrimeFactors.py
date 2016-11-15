import sys 
import os
import time
import math
sys.path.append(os.path.abspath("../Algorithms/"))

from ESieve import ESieve 

def primeFactorsNoCache(num):

  if num == 0:
    return {}

  factors={}
  startNum=num

  while num % 2 == 0:
    factors[2]=factors.get(2,0)+1
    num /= 2

  i=3
  maxPos=math.sqrt(num)

  while i <= maxPos:
    if num % i == 0:
      factors[i]=factors.get(i,0)+1
      num /= i
    else:
      i+=2

    if num > 1 and num <> startNum:
      factors[num]=factors.get(num,0)+1

  return factors

def primeFactors(num, primesCache=ESieve(1000000)):

  if num == 0:
    return {}

  factors={}
  startNum=num

  maxPos=math.sqrt(num)
  for i in range(len(primesCache)):
    if primesCache[i] > maxPos:
      break
    while num % primesCache[i] == 0:
      factors[primesCache[i]]=factors.get(primesCache[i],0)+1
      num /= primesCache[i]

  if num > 1 and num <> startNum:
    factors[num]=factors.get(num,0)+1

  return factors

def numberOfFactors(num, primesCache=ESieve(1000000)):

  count = 1
  for exp in primeFactors(num,primesCache).values():
    count *= (exp+1)

  return count

def numberOfFactorsOfSquare(num, primesCache=ESieve(1000000)):

  count = 1
  for exp in primeFactors(num,primesCache).values():
    count *= (exp*2+1)
  return count

def allFactors(num, primesCache=ESieve(1000000)):
  factors = primeFactors(num,primesCache).items()
  nfactors = len(factors)
  if nfactors < 1:
    yield 1
    if num > 1:
      yield num
      return

    f = [0] * nfactors

    while True:
      yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
      i = 0
      while True:
        f[i] += 1
        if f[i] <= factors[i][1]:
          break
        f[i] = 0
        i += 1
        if i >= nfactors:
          return

#testNum=48
#print numberOfFactors(testNum,ESieve(math.sqrt(testNum)))
