import itertools

string="0123456789"

primes=[2,3,5,7,11,13,17]

start=1
length=3
lengthStr=len(string)

result=0

x = list(itertools.permutations(string))
for pd in x:
    pdString="".join(pd)
    found=True
    for i in range(1,8):
        if not (int(pdString[i:min(lengthStr,(i+3))]) % primes[(i-1)] == 0):
               found=False
    if found:
        result+=int(pdString)

print "Result:",result
        
