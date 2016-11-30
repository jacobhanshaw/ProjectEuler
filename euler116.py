
def F(m, n, cache):

  count = 1

  if(m > n):
    return count

  if(cache[n] > 0):
    return cache[n]

  for startIndex in range(0, n-m+1):
    count += F(m, n - startIndex - m, cache)

  cache[n] = count
  return count

count = 0
n = 50
mMin = 2
mMax = 4
for m in range(mMin, mMax + 1):
  cache = [0] * (n+1)
  count += F(m, n, cache) - 1

print count
