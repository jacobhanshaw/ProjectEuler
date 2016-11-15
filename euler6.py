
number=100
power=2

def GaussianSum(n):
    return (n * (n+1))/2

SquareOfSums=pow(GaussianSum(number),power)

SumOfSquares=0

for i in range(1,(number+1),1):
    SumOfSquares+=pow(i,power)


print "Result: ",(SquareOfSums-SumOfSquares)
