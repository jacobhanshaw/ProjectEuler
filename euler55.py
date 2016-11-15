

def isPalindrome(num):
    string=str(num)
    for i in range(0,len(string)/2,1):
        if string[i] <> string[len(string)-1-i]:
            return False

    return True

def constructOpposite(num):
    string=str(num)
    result=""
    for i in range(len(string)-1,-1,-1):
        result+=string[i]

    return int(result)

result=0
neededCount=50

for i in range(1,10000):
    num=i
    count=0
    palindrome=False
    while not palindrome and count < neededCount:
        count+=1
        num+=constructOpposite(num)
        palindrome=isPalindrome(num)
    if count == neededCount:
        result+=1

print "Result:",result
