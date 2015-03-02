"""
To be odd must be even+odd.
Mirror numbers won't work as both will be even or odd.
Counting odds will be half of total (there is an even pair to each)
and skip the 10's (which cause leading 0's)
Most sig fig must be even then, so least sig fig is upon reversal
"""


def reverse(num):
    strNum=str(num)
    result=""

    for i in range(len(strNum)-1,-1,-1):
        result+=strNum[i]

    return int(result)
"""
    reversedNum=0
    while num > 0:
        reversedNum = 10 * reversedNum + num % 10;
        num /= 10;

    return reversedNum
"""
def allOdd(num):

    while num > 0:
        if num % 2 == 0:
            return False
        num = num // 10

    return True

num=21
nextNumInc=10

count=0
while num < 1000000000:
    print num
    lenNextNumInc=len(str(nextNumInc))
    while len(str(num)) == lenNextNumInc:
        nextRange=num+nextNumInc
        while num < nextRange:
            testNum=num+reverse(num)
            if allOdd(testNum):
                count+=1
            num+=2
        num+=nextNumInc
        
    nextNumInc*=10
    num+=nextNumInc

print "Count:",count*2
