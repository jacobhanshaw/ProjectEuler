import math

goalPermutation=999999

nums=["0","1","2","3","4","5","6","7","8","9"]
result=""

currentFactorial=len(nums)-1

while len(nums) > 1:
    factorial=math.factorial(currentFactorial)
    currentFactorial-=1
    index=goalPermutation/factorial
    goalPermutation-=index*factorial
    result+=nums.pop(index)

result+=nums.pop(0)

print "Result: ",result



"""
def swap(c, i, j):
    if(i==j):
        print "Waste"
        return c
    
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return "".join(c)

def permute(string,start,end,rList):
    if(start==end):
        rList.append(string)
    else:
        for i in range(start,end+1,1):
            string=swap(string,start,i)
            permute(string,start+1,end,rList)
            string=swap(string,start,i)           

string="0123456789"


rList=[]
permute(string,0,len(string)-1,rList)
rList.sort()
print "String: ",rList[999999]
"""

#Answer: 2783915460
