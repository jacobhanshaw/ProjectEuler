"""
Break when len(num**power) < power
End num==10 as 10+ len(num**power) always > power
"""

result=0

num=1
power=1

while num < 10:
    string=str(num**power)
    if len(string)==power:
        result+=1
    elif len(string) < power:
        num+=1
        power=0 #will be incremented to 1
    power+=1
    
print "Result:",result
