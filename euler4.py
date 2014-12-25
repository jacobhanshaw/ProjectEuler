
def largestPalindrome(base):
    base = int(str(base) + str(base)[2] + str(base)[1] + str(base)[0])

    for i in range(999,100,-1):
        
        if base % i == 0 and base/i < 999:
            return base

    return -1

result = []

for i in range(999,100,-1):
    result = largestPalindrome(i)

    if result <> -1:
        break

print result
