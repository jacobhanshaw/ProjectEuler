import sys 
import os
sys.path.append(os.path.abspath("../Algorithms/"))

from SumDigits import sumDigits

a = []

for b in range(2,400):
  value = b
  for e in range(2,50):
    value *= b

    if sumDigits(value) == b:
      a.append(value)

    if(len(a) > 50):
      break

  if(len(a) > 50):
    break

a.sort()

print "Result: ", a[29]
