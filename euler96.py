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

    firstLoop = True
    unknownPoints={}
    
    while len(unknownPoints) or firstLoop:
        
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
# May comment \/ out as it is redundant, may be quicker to do both though
                eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInBox[i][j],unknownPoints)
                eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInBox[i][j],unknownPoints)

        for i in range(len(sudoku)):
            eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInRow[i],unknownPoints)
            eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInRow[i],unknownPoints)

        for i in range(len(sudoku[0])):
            eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInCol[i],unknownPoints)
            eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInCol[i],unknownPoints)

        firstLoop=False
                
def eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsKeys,unknownPoints):
    
    for originalKey in unknownPointsKeys:
        originalVal=unknownPoints[originalKey]
        rest=unknownPoints.copy()
        rest.pop(originalKey,None)

        firstDiff=True
        differences=set()
        sameKeys=[originalKey]
        for key,val in rest.items():
            newDiff=originalVal.difference(val)
            if len(newDiff) == 0:
                differences=set()
                break
            if len(differences) == 0:
                if firstDiff:
                    firstDiff=False
                    differences=differences.union(newDiff)
                else:
                    differences=set()
                    break
            else:
                differences=differences.intersection(newDiff)

        if len(differences) == 1:
            rowCol=decodeKey(originalKey)
            setPoint(sudoku,rowCol[0],rowCol[1],differences.pop(),unusedGroup,unknownPointsGroup,unknownPoints,originalKey)

def eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsKeys,unknownPoints):
    lenPoints=len(unknownPointsKeys)
    if lenPoints == 1:
        key=unknownPointsKeys[0]
        rowCol=decodeKey(key)
        setPoint(sudoku,rowCol[0],rowCol[1],unknownPoints[key].pop(),unusedGroup,unknownPointsGroup,unknownPoints,key)
        return
    
    f = [0] * lenPoints

    i = 0
    count=0
    while i < lenPoints:
        if count > 1:
            otherKeys=[]
            allOptions=set()
            for j in range(lenPoints):
                if f[j] == 1:
                    allOptions=allOptions.union(unknownPoints[unknownPointsKeys[j]])
                else:
                    otherKeys.append(unknownPointsKeys[j])
            
            if count >= len(allOptions):
                for key in otherKeys:
                    rowCol=decodeKey(key)
                    removeOptions(sudoku,rowCol[0],rowCol[1],allOptions,unusedGroup,unknownPointsGroup,unknownPoints,key)
        i = 0
        while i < lenPoints:
            f[i] += 1
            count+= 1
            if f[i] <= 1:
                break
            count-= f[i]
            f[i] = 0
            i += 1

    for key in unknownPointsKeys:
        if len(unknownPoints[key]) == 1:
            rowCol=decodeKey(key)
            setPoint(sudoku,rowCol[0],rowCol[1],unknownPoints[key].pop(),unusedGroup,unknownPointsGroup,unknownPoints,key)
            
def makeKey(row,col):
    return (row+1)*10+(col+1)
                
def decodeKey(key):
    return ((key//10-1),(key%10-1))

def setPoint(sudoku,row,col,value,unusedGroup,unknownPointsGroup,unknownPoints,key):
#    print "Make:",row,col,"to",value
    sudoku[row][col]=value

    unusedGroup[Group.ROW.value][row].remove(value)
    unusedGroup[Group.COL.value][col].remove(value)
    unusedGroup[Group.BOX.value][row//3][col//3].remove(value)

    try:
        unknownPointsGroup[Group.ROW.value][row].remove(key)
    except ValueError:
        pass
    try:
        unknownPointsGroup[Group.COL.value][col].remove(key)
    except ValueError:
        pass
    try:
        unknownPointsGroup[Group.BOX.value][row//3][col//3].remove(key)
    except ValueError:
        pass

    valueSet=set([value])
    unknownPoints.pop(key,None)

    for key in unknownPointsGroup[Group.ROW.value][row]:
        unknownPoints[key]=unknownPoints[key].difference(valueSet)
        
    for key in unknownPointsGroup[Group.COL.value][col]:
        unknownPoints[key]=unknownPoints[key].difference(valueSet)
        
    for key in unknownPointsGroup[Group.BOX.value][row//3][col//3]:
        unknownPoints[key]=unknownPoints[key].difference(valueSet)

def removeOptions(sudoku,row,col,options,unusedGroup,unknownPointsGroup,unknownPoints,key):    
    unknownPoints[key]=unknownPoints[key].difference(options)
                
def getUnusedInRow(sudoku,rows,row):
    if len(rows[row]) > 0:
        return rows[row]

    notInRow=[1,2,3,4,5,6,7,8,9]

    for i in range(len(sudoku[0])):
        current=sudoku[row][i] 
        if current <> 0:
            notInRow.remove(current)

    rows[row]=notInRow
    
    return notInRow

def getUnusedInCol(sudoku,cols,col):
    if len(cols[col]) > 0:
        return cols[col]

    notInCol=[1,2,3,4,5,6,7,8,9]

    for i in range(len(sudoku)):
        current=sudoku[i][col] 
        if current <> 0:
            notInCol.remove(current)

    cols[col]=notInCol
    
    return notInCol

def getUnusedInBox(sudoku,boxes,row,col):
    if len(boxes[row][col]) > 0:
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

#Should be unnecessary
def getUnusedByUnknownPoints(unknownPointsKeys,unknownPoints):
    allUnknown=unknownPoints[unknownPointsKeys[0]]

    for i in range(1,len(unknownPointsKeys)):
        allUnknown=allUnknown.union(unknownPoints[unknownPointsKeys[i]])

    return allUnknown

def getBox(sudoku,row,col):

    box=[]
    for i in range(3):
        currentRow=[]
        for j in range(3):
            currentRow.append(sudoku[row*3+i][col*3+j])
        box.append(currentRow)

    return box

def printSudoku(sudoku):
    for i in range(len(sudoku)):
        print sudoku[i]

def validSudoku(sudoku):
    valid=True

    rows=[[],[],[],[],[],[],[],[],[]]
    for i in range(len(sudoku)):
        valid &= len(getUnusedInRow(sudoku,rows,i))==0

    cols=[[],[],[],[],[],[],[],[],[]]
    for i in range(len(sudoku[0])):
        valid &= len(getUnusedInCol(sudoku,cols,i))==0

    boxes=[[[],[],[]],[[],[],[]],[[],[],[]]]
    for i in range(3):
        for j in range(3):
            valid &= len(getUnusedInBox(sudoku,boxes,i,j))==0

    return valid

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

    print "Before:"
    printSudoku(sudoku)
    solveSudoku(sudoku)
    print "After:"
    printSudoku(sudoku)

    print "Valid:",validSudoku(sudoku)

    sumOfTopLeft+= 100 * sudoku[0][0] + 10 * sudoku[0][1] + sudoku[0][2]
    line=sudokuFile.readline()

print "Result: ",sumOfTopLeft
