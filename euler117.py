
def F(mMin, mMax, n, cache):

  count = 1

  if(mMin > n):
    return count

  if(cache[n] > 0):
    return cache[n]

  for blockLength in range(mMin, mMax+1):
    for startIndex in range(0, n-blockLength+1):
      count += F(mMin, mMax, n - startIndex - blockLength, cache)

  cache[n] = count
  return count

n = 50
mMin = 2
mMax = 4
cache = [0] * (n+1)
print F(mMin, mMax, n, cache)
