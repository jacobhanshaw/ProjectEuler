import math
#6  1 2 3 6


#16 1 2 4 8 16
#26 1 2 13 26
#36 1 2 4 6 9 18 36
#46 1 2 23 46
#56 1 2 4 ...
#66 1 2 6 11 33 66

#14 1 2 7 14
#24 1 2 3 4 6 8 12 24
#34 1 2 17 34
"""
Not:
  Odds
  4
  8
  12
  14
  16
  18
  24
  """

#Can skip all odd (except) 1 as all other even nums are not prime
#Can skip divisible by 4 as will be divisible by 2 and another even num
#Can skip all ending in four as one plus num will be divisible by 5
#Can skip all ending in six (except for 6) as either divisble by 4 or 2 and a number ending in three (divisible by 5)
#Can skip even (when/10) ending in zero at (20, 2840, etc.) as divisible by 20 (and 4)
#Can skip even (when/10) ending in eight (divisible by four)

#Left with:
  #odd followed by zero or eight
  #even followed by two

def binarySearchArray(array,goal):
  low=0
  high=len(array)-1
  while low<=high:
    mid=(high+low)//2
    current=array[mid]
    if goal < current:
      high=mid-1
    elif goal > current:
      low=mid+1
    else:
      return mid

    return -1

def primeCheck(n,primes):
  lenNum = len(str(n))

  if lenNum < len(primes):
    return binarySearchArray(primes[lenNum],n) <> -1

  return isPrime(n)

def isPrime(n):
  if n % 3==0:
    return False
  else:
    r=math.floor(math.sqrt(n)) # n rounded to the greatest integer r so that r*r<=n
    f=5
    while f<=r:
      if n % f==0:
        return False
      if n % (f+2) == 0:
        return False
      f=f+6

    return True

def primeFactors(num):

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

def allFactors(num):
  factors = primeFactors(num).items()
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

def sumOfFactorsArePrime(num,primes):
  factors = list(allFactors(num))
  factors.sort()
  lenFactors = len(factors)

  center = (lenFactors/2.0)
  if not center.is_integer():
    return False
  for i in range(int(center)):
    combined=(factors[i]+factors[(lenFactors-i-1)])
    if not primeCheck(num,primes):
      return False

  return True

primes = [[]]
primes.append([2,3,5,7])
total = 9 #pre-add in one,two, and six
maxNum = 100000000

#Left with:
  #odd followed by zero or eight
  #even followed by two

print "Start"

num = 11
nextMax = 100
numLen = 2
maxLen = len(str((maxNum+1)))
while numLen < 7:    #= maxLen: #maxLen:
  primes.append([])
  while num < nextMax:
    if isPrime(num):
      primes[numLen].append(num)
      num += 2
      numLen += 1
      nextMax *= 10

      """
      primes.append([])
      if isPrime((maxNum+1)):
        primes[maxLen].append((maxNum+1))
        """

print "Primes Done"

for num in range(22,maxNum+1,20):
  if sumOfFactorsArePrime(num,primes):
    total += num

print "2's Done"

for num in range(10,maxNum+1,20):
  if sumOfFactorsArePrime(num,primes):
    total += num

print "0's Done"

for num in range(18,maxNum+1,20):
  if sumOfFactorsArePrime(num,primes):
    total += num

print "8's Done"

print "Result:",total
