import math

number=100

factorial=math.factorial(number)
stringFactorial=str(factorial)

result=0

for i in range(0,len(stringFactorial),1):
    result+=int(stringFactorial[i])

print "Result: ",result
