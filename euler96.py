from enum import Enum

class Group(Enum):
    ROW=0
    COL=1
    BOX=2
    LEN=3

def solveSudoku(sudoku):
    rows=[[],[],[],[],[],[],[],[],[]]
    cols=[[],[],[],[],[],[],[],[],[]]
    boxes=[[[],[],[]],[[],[],[]],[[],[],[]]]
    unusedGroup=[rows,cols,boxes]

    unknownPointsInRow=[[],[],[],[],[],[],[],[],[]]
    unknownPointsInCol=[[],[],[],[],[],[],[],[],[]]
    unknownPointsInBox=[[[],[],[]],[[],[],[]],[[],[],[]]]
    unknownPointsGroup=[unknownPointsInRow,unknownPointsInCol,unknownPointsInBox]

    do = True
    unknownPoints={}
    
    while len(unknownPoints) or do:
        do=False
        
        for i in range(len(sudoku)):
            for j in range(len(sudoku[0])):
                current=sudoku[i][j]
                if sudoku[i][j] == 0:
                    rowOptions=getUnusedInRow(sudoku,rows,i)
                    colOptions=getUnusedInCol(sudoku,cols,j)
                    boxOptions=getUnusedInBox(sudoku,boxes,i//3,j//3)
                    options=set(boxOptions).intersection(colOptions).intersection(rowOptions)

                    key=makeKey(i,j)
                    alreadyUnknownPoint=(key in unknownPoints)
                    
                    if alreadyUnknownPoint:
                        options=options.intersection(unknownPoints[key])

                    if len(options) == 1:
                        setPoint(sudoku,i,j,options.pop(),unusedGroup,unknownPointsGroup,unknownPoints,key)
                    else:
                        if not alreadyUnknownPoint:
                            unknownPointsInRow[i].append(key)
                            unknownPointsInCol[j].append(key)
                            unknownPointsInBox[i//3][j//3].append(key)
                        unknownPoints[key]=options

        for i in range(3):
            for j in range(3):
                print "Box:",i,j
#                print "Box before:",getBox(sudoku,i,j)
                eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInBox[i][j],unknownPoints)
#                print "Box after :",getBox(sudoku,i,j)

        for i in range(len(sudoku)):
            print "Row:",i
#            print "Row before:",getUnsolvedInRow(sudoku,rows,i)
            eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInRow[i],unknownPoints)
#            print "Row after :",getUnsolvedInRow(sudoku,rows,i)

        for i in range(len(sudoku[0])):
            print "Col:",i
#            print "Col before:",getUnsolvedInCol(sudoku,cols,i)
            eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInCol[i],unknownPoints)
#            print "Col after :",getUnsolvedInCol(sudoku,cols,i)

                
def eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsKeys,unknownPoints):
    
    for originalKey in unknownPointsKeys:
        originalVal=unknownPoints[originalKey]
        rest=unknownPoints.copy()
        rest.pop(originalKey,None)

#        print unknownPoints
         
#        print "Start", decodeKey(originalKey),originalVal
        skipDiff=False
        firstDiff=True
        differences=set()
        sameKeys=[originalKey]
        for key,val in rest.items():
            if val == originalVal:
                sameKeys.append(key)
#            print "Test Against:",decodeKey(key),val
            newDiff=originalVal.difference(val)
            if not skipDiff:
                if len(newDiff) == 0:
                    skipDiff=True
                if len(differences) == 0:
                    if firstDiff:
#                        print "First Go",newDiff
                        firstDiff=False
                        differences=differences.union(newDiff)
                    else:
                        skipDiff=True
                else:
#                    print "EB:",differences,newDiff
                    differences=differences.intersection(newDiff)
#                    print "Next",differences

        if len(differences) == 1:
 #           print "DO KEY:",decodeKey(originalKey),differences
#            print "Before:",sudoku[originalKey//10-1][originalKey%10-1]
            sudoku[originalKey//10-1][originalKey%10-1]=differences.pop()
#            print "After:",sudoku[originalKey//10-1][originalKey%10-1]
 #           print "Before:",unknownPoints,rest
            print "Diff Make:",(originalKey//10-1),(originalKey%10-1),"to",sudoku[originalKey//10-1][originalKey%10-1]
            unknownPoints.pop(originalKey,None)
            rest.pop(originalKey,None)
#            print "After:",unknownPoints,rest

        if len(originalVal) == len(sameKeys):
#            print "Rest:",rest
            for key,val in rest.items():
                if (not isinstance(val, (int, long))) and val <> originalVal:
                    print "SO KEY:",decodeKey(key)
                    print "Before:",sudoku[key//10-1][key%10-1]
                    sudoku[key//10-1][key%10-1]=val.difference(originalVal)
                    print "After:",sudoku[key//10-1][key%10-1]
                    if len(sudoku[key//10-1][key%10-1])==1:
                        sudoku[key//10-1][key%10-1]=sudoku[key//10-1][key%10-1].pop()
                        print "Same Make:",(key//10-1),(key%10-1),"to",sudoku[key//10-1][key%10-1]
                        unknownPoints.pop(key,None)
                        rest.pop(key,None)

def makeKey(row,col):
    return (row+1)*10+(col+1)
                
def decodeKey(key):
    return ((key//10-1),(key%10-1))

def setPoint(sudoku,row,col,value,unusedGroup,unknownPointsGroup,unknownPoints,key):
    print "Set Make:",row,col,"to",value
    sudoku[row][col]=value

    unusedGroup[Group.ROW.value][row].remove(value)
    unusedGroup[Group.COL.value][col].remove(value)
    unusedGroup[Group.BOX.value][row][col].remove(value)

    unknownPointsGroup[Group.ROW.value][row].remove(key)
    unknownPointsGroup[Group.COL.value][col].remove(key)
    unknownPointsGroup[Group.BOX.value][row][col].remove(key)
    
    unknownPoints.pop(key,None)
                
def getUnusedInRow(sudoku,rows,row):
    if row < len(rows):
        return rows[row]

    notInRow=[1,2,3,4,5,6,7,8,9]

    for i in range(len(sudoku[0])):
        current=sudoku[row][i] 
        if current <> 0:
            notInRow.remove(current)

    print row
    rows[row]=notInRow
    
    return notInRow

def getUnusedInCol(sudoku,cols,col):
    if col < len(cols):
        return cols[col]

    notInCol=[1,2,3,4,5,6,7,8,9]

    for i in range(len(sudoku)):
        current=sudoku[i][col] 
        if current <> 0:
            notInCol.remove(current)

    cols[col]=notInCol
    
    return notInCol

def getUnusedInBox(sudoku,boxes,row,col):
    if row < len(boxes) and col < len(boxes[row]):
        return boxes[row][col]  
    
    notInBox=[1,2,3,4,5,6,7,8,9]
    for i in range(3):
        currentRow=[]
        for j in range(3):
            current= sudoku[row*3+i][col*3+j]
            if current <> 0:
                notInBox.remove(current)

    boxes[row][col]=notInBox
    
    return notInBox

def getBox(sudoku,row,col):

    box=[]
    for i in range(3):
        currentRow=[]
        for j in range(3):
            currentRow.append(sudoku[row*3+i][col*3+j])
        box.append(currentRow)

    return box

sudokuRows=9
sudokuCols=9

sudokuFile = open("p096_sudoku.txt")

sumOfTopLeft=0
line=sudokuFile.readline()
while line <> "":
    sudoku=[]
    for i in range(sudokuRows):
        sudokuLine=sudokuFile.readline()
        sudokuRow=[]
        for j in range(sudokuCols):
            sudokuRow.append(int(sudokuLine[j]))
        sudoku.append(sudokuRow)

    print sudoku
    solveSudoku(sudoku)

    sumOfTopLeft+= 100 * sudoku[0][0] + 10 * sudoku[0][1] + sudoku[0][2]
    line=sudokuFile.readline()

print "Result: ",sumOfTopLeft
