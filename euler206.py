from math import sqrt
from math import ceil
"""
Num must end in zero, so whatever is squared must end in zero.

Brute force fail. Likely pattern in increase.
"""

def test(num):
    goal=1
    strNum=str(num)
    for i in range(0,19,2):
        if strNum[i] <> str(goal):
            return False

        goal+=1
        
    if strNum[18] <> '0':
        return False

    return True
    
    
minNum=1020304050607080900
maxNum=1929394959697989990

num = sqrt(minNum)
if num.is_integer():
    print "Result:",num
else:
    num=ceil(num)
    square=num**2
    while not test(square) and square < maxNum:
        num+=10
        square=num**2
        print "N:",num,"S:",square
