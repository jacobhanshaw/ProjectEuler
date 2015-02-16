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
#                print "Box:",i,j
#                print "Box before:",getBox(sudoku,i,j)
                eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInBox[i][j],unknownPoints)
                eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInBox[i][j],unknownPoints)
#                print "Box after :",getBox(sudoku,i,j)

        for i in range(len(sudoku)):
#            print "Row:",i
#            print "Row before:",getUnsolvedInRow(sudoku,rows,i)
            eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInRow[i],unknownPoints)
            eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInRow[i],unknownPoints)
#            print "Row after :",getUnsolvedInRow(sudoku,rows,i)

        for i in range(len(sudoku[0])):
#            print "Col:",i
#            print "Col before:",getUnsolvedInCol(sudoku,cols,i)
            eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInCol[i],unknownPoints)
            eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInCol[i],unknownPoints)
#            print "Col after :",getUnsolvedInCol(sudoku,cols,i)

        firstLoop=False

                
def eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsKeys,unknownPoints):
    
    for originalKey in unknownPointsKeys:
        originalVal=unknownPoints[originalKey]
        rest=unknownPoints.copy()
        rest.pop(originalKey,None)
         
#        print "Start", decodeKey(originalKey),originalVal
        firstDiff=True
        differences=set()
        sameKeys=[originalKey]
        for key,val in rest.items():
#            print "Test Against:",decodeKey(key),val
            newDiff=originalVal.difference(val)
            if len(newDiff) == 0:
                differences=set()
                break
            if len(differences) == 0:
                if firstDiff:
#                    print "First Go",newDiff
                    firstDiff=False
                    differences=differences.union(newDiff)
                else:
                    differences=set()
                    break
            else:
#                print "EB:",differences,newDiff
                differences=differences.intersection(newDiff)
#                print "Next",differences

        if len(differences) == 1:
            rowCol=decodeKey(originalKey)
            setPoint(sudoku,rowCol[0],rowCol[1],differences.pop(),unusedGroup,unknownPointsGroup,unknownPoints,originalKey)

def eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsKeys,unknownPoints):
    #factors = primeFactors(num).items()
    lenPoints=len(unknownPointsKeys)
 #   if lenPoints == 1:
#        key=unknownPointsKeys[0]
#        rowCol=decodeKey(key)
#        print "RC:",rowCol
#        print "Key:",key
#        print "UnknownPointsKeys:",unknownPointsKeys
#        print "UnknownPoints:",unknownPoints
#        print "UNUSED:",unusedGroup
#        setPoint(sudoku,rowCol[0],rowCol[1],unknownPoints[key].pop(),unusedGroup,unknownPointsGroup,unknownPoints,key)
#        return
    
    f = [0] * lenPoints

    i = 0
    count=0
    while i < lenPoints:
        if count > 1:
            otherKeys=[]
            allOptions=set()
            #print f
            for j in range(lenPoints):
                if f[j] == 1:
                    #print "Unknown:",unknownPoints[unknownPointsKeys[j]]
                    allOptions=allOptions.union(unknownPoints[unknownPointsKeys[j]])
                else:
                    otherKeys.append(unknownPointsKeys[j])

            #print count,allOptions
            
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
            
def makeKey(row,col):
    return (row+1)*10+(col+1)
                
def decodeKey(key):
    return ((key//10-1),(key%10-1))

def setPoint(sudoku,row,col,value,unusedGroup,unknownPointsGroup,unknownPoints,key):
#    print "Make:",row,col,"to",value
    sudoku[row][col]=value

#    if row == 1:
#        print "Before",unusedGroup[Group.ROW.value][row],value
    if len(unusedGroup[Group.ROW.value][row]) > 0:
        unusedGroup[Group.ROW.value][row].remove(value)
    if len(unusedGroup[Group.COL.value][col]) > 0:
        unusedGroup[Group.COL.value][col].remove(value)
    if len(unusedGroup[Group.BOX.value][row//3][col//3]) > 0:
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
    
    unknownPoints.pop(key,None)

def removeOptions(sudoku,row,col,options,unusedGroup,unknownPointsGroup,unknownPoints,key):
#    if row == 1 and col == 2:
#        print "Remove:",row,col,"options",options

    unusedGroup[Group.ROW.value][row]=[]
    unusedGroup[Group.COL.value][col]=[]
    unusedGroup[Group.BOX.value][row//3][col//3]=[]
    
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

    print "Before:",sudoku
    solveSudoku(sudoku)
    print "After:",sudoku

    sumOfTopLeft+= 100 * sudoku[0][0] + 10 * sudoku[0][1] + sudoku[0][2]
    line=sudokuFile.readline()

print "Result: ",sumOfTopLeft
