
def F(m, n, cache):

  count = 1

  if(m > n):
    return count

  if(cache[n] > 0):
    return cache[n]

  for startIndex in range(0, n-m+1):
    for blockLength in range(m, n-startIndex+1):
      count += F(m, n - startIndex - blockLength - 1, cache)

  cache[n] = count
  return count

n = 50
m = 3
cache = [0] * (n+1)
print "114: " + str(F(m, n, cache))

m = 50
n = m - 1
count = 0
goal = 10**6
cache = [0] * 200 # Rough upper bound

while count <= goal:
  n += 1
  count = F(m, n, cache)

print "115: " + str(n)
