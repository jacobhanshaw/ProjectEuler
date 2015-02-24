
def isPalindrome(num):
    strNum=str(num)
    midStr = len(strNum)//2
    
    if midStr == 0 or strNum[:midStr]==strNum[-midStr:][::-1]:  
        return True
    
    return False

def square(index,squares):
    if index >= len(squares):
        squares.append((index+1)**2)

    return squares[index]

squares=[]
palindromeSums=[]

do = True
baseIndex=0

total=0
maxSum = 10**8

while do or squares[baseIndex] < maxSum:
    do = False

    squaresIndex=baseIndex+1
    palindromeSum=square(baseIndex,squares)+square(squaresIndex,squares)
    while palindromeSum < maxSum:
        if isPalindrome(palindromeSum) and palindromeSum not in palindromeSums:
            palindromeSums.append(palindromeSum)
            total+=palindromeSum
            
        squaresIndex+=1
        palindromeSum+=square(squaresIndex,squares)
        
    baseIndex += 1

print "Result:",total
