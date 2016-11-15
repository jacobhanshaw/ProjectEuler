"""
There's a pattern
Denominator = next numerator-denominator
Denominator+Numerator = next denominator
3/2
7/5 (1+2/5)
17/12 (1+5/12)
41/29 (1+12/29)
"""

numerator=3
denominator=2

expansion=1
expansions=1000

result = 0

while expansion < expansions:
    tmpDenominator=denominator
    denominator+=numerator
    numerator=tmpDenominator+denominator
    
    if len(str(numerator)) > len(str(denominator)):
        result+=1

    expansion+=1

print "Result:",result
