

def isPalindrome(string):
    for i in range(0,len(string)/2,1):
        if string[i] <> string[len(string)-1-i]:
            return False

    return True

def constructEvenPalindrome(string):
    for i in range(len(string)-1,-1,-1):
        string+=string[i]

    return string

def constructOddPalindrome(string):
    for i in range(len(string)-2,-1,-1):
        string+=string[i]

    return string

result=0

for i in range(1,1000,1):
    palindrome=int(constructOddPalindrome(str(i)))
    if isPalindrome(bin(palindrome)[2:]):
        result+=palindrome
    palindrome=int(constructEvenPalindrome(str(i)))
    if isPalindrome(bin(palindrome)[2:]):
        result+=palindrome

print "Result: ",result
