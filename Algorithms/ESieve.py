from bitarray import bitarray
from math import sqrt
from math import log

def ESieve(upperLimit):
  sieveBound = int((upperLimit - 1) / 2)
  upperSqrt = int(round(sqrt(upperLimit) - 1) / 2)
  
  primeBits = bitarray(sieveBound+1)
  primeBits.setall(True)

  for i in range(1,(upperSqrt+1)):
    if primeBits[i]:
      for j in range(i * 2 * (i+1), (sieveBound+1), (i * 2 + 1)):
        primeBits[j] = False

  numbers = []
  numbers.append(2);
  for i in range(1, (sieveBound +1)): 
    if primeBits[i]:
      numbers.append(2 * i + 1);
    
  return numbers
