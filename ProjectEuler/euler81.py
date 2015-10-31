numbersFile = open("matrix.txt")

matrix=[]

for line in numbersFile:
    matrix.append(line.rstrip().split(","))

"""
def minPath(matrix,row,col):
    if row == 0 and col == 0:
        return 0
    if row < 0 or col < 0:
        return 99999999999999
    
    return int(matrix[row][col]) + min(minPath(matrix,row-1,col),minPath(matrix,row,col-1))

print "Min Path:",minPath(matrix,len(matrix)-1,len(matrix[0])-1)
"""

matrixWidth=len(matrix[0])
matrixHeight=len(matrix)

for j in range(matrixWidth-1,-1,-1):
    for i in range(matrixHeight-1,-1,-1):
        down=-1
        right=-1
        if j+1 < matrixWidth:
            right=int(matrix[i][j+1])
        if i+1 < matrixHeight:
            down=int(matrix[i+1][j])
            
        minValue=0
        if down<>-1 and right<>-1:
            minValue=min(right,down)
        elif down<>-1 or right<>-1:
            if down==-1:
                minValue=right
            elif right==-1:
                minValue=down

        matrix[i][j]=int(matrix[i][j])+minValue

print "Result:",matrix[0][0]
