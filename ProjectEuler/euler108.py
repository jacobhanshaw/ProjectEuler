import sys 
import os
sys.path.append(os.path.abspath("../Algorithms/"))

from ESieve import ESieve
from PrimeFactors import numberOfFactors
from PrimeFactors import numberOfFactorsOfSquare

goalSolutions = 1000

#x,y must be < n and the max x is 2*n before solutions repeat with x & y swapped
#therefore, n must be at least 2*goalSolutions+1 to have more than goalSolutions
#solutions

n=goalSolutions*2+1 
primesCache = ESieve(20000) 

def NoDSquared(number,primelist): 
  nod = 1
  exponent = 1
  remain = number

  for i in range(len(primelist)):
    if primelist[i] * primelist[i] > number:
      return nod * 2

    exponent = 1
    while remain % primelist[i] == 0:
      exponent+=2
      remain = remain / primelist[i]
   
    nod *= exponent;
   
    if remain == 1:
      return nod
  
  return nod

while(True):
  myNum = numberOfFactorsOfSquare(n,primesCache)
  #num = NoDSquared(n,primesCache)
  if (myNum+1)/2 > goalSolutions:
    print "Result: ",n
    break

  n+=1
