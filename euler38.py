import itertools

#Pretty wasteful.
#Only the first 4-digits of the permutations are really used
#The algorithm cycles through all possible combinations of next 5-digits, but
#I could just generate the rest of the number according to the formula
#and check if it passes the pandigital test. Would still have to check
#3-digit and 2-digit bases to not leverage my knowledge of the answer, but
#my implementation would be to check those on start and every time those digits
#are swapped, so:
#9876:check 98,987, and 9876
#9875:only need check 9875
#...
#9867:check 986 and 9867
#...
#9786:check 97,978, and 9786
#
#May get back around to this.

"""
Given Answer is > 918273645 using x = 9
First concatenation is x * 1
Since x=9 is largest single-wide and not the answer
and the number must be > 918273645 (Which would mean >= 92...)
x must be 2, 3, or 4 digits wide and begin with 9
"""

failed=True
string="123456789"
greatestFailed=""
x = list(itertools.permutations(string))
for i in range(len(x)-1,-1,-1):
    value = "".join(x[i])
    for digitWidth in range(2,5):
        number=int(value[:digitWidth])
        mult=2
        failed=True
        start=digitWidth
        while start < len(string):
            nextChunk=number*mult
            lenNextChunk=len(str(nextChunk))
            nextStart=start+lenNextChunk
            if not int(value[start:nextStart])==nextChunk:
                break
            start=nextStart
            if nextStart == len(string):
                failed=False
                break
            mult+=1
        if not failed:
            break
    if not failed:
            print "Result: ",value
            break
