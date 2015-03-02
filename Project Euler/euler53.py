from math import factorial

factorials=[]

for i in range(0,101,1):
    factorials.append(factorial(i))

result=0
for n in range(100,1,-1):
    for r in range(i-1,0,-1):
        if factorials[n]/(factorials[r]*factorials[(n-r)]) > 1000000:
            result+=1

print "Result: ",result
