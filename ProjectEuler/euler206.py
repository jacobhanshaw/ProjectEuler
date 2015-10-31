from math import sqrt
from math import ceil
"""
Num must end in zero, so whatever is squared must end in zero.

Brute force fail. Likely pattern in increase.

Has to end in zero for square to end in zero
Given /\ must end in 30 or 70 to have 9_0

Can skip check on first character - due to range limitations (minNum-maxNum)
And can skip last 3 as the num squraed will always end in 30 and produce 900
Otherwise, can skip every other character as per instructions
"""

def test(num):
    goal=2
    strNum=str(num)
    for i in range(2,15,2):
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
    num=int(ceil(num))
    num-=(num % 100)
    num+=30           #start num ending in 30

    square=num**2                 
    while not test(square) and square < maxNum: 
        num+=40       #if not try ending in 70
        square=num**2
        if test(square) or square > maxNum:
            break
        num+=60       #back to 30
        square=num**2
            
        
print "N:",num,"S:",square
