from enum import Enum

#AVOIDING GLOBALS GOT SUPER MESSY

#NEED TO TRACK ALL COMPUTER CHOICES SINCE GUESSING STARTED

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

    lastCount=-1
    firstLoop = True
    unknownPoints={}

    badGuess=False
    guessedKeys=[]
    unguessedValues={}
    currentGuessAlternateOptions=set([])

    startedGuessing=False
    filledWhileGuessingKeys=[]
    filledWhileGuessingValues={}
    filledWhileGuessingOptions={}
    
    while len(unknownPoints) or firstLoop:

        if len(unknownPoints) == lastCount or badGuess:
            print "Guessing"

#            if startedGuessing and badGuess:

#                    startedGuessing,filledWhileGuessingKeys,filledWhileGuessingValues,filledWhileGuessingOptions
            
            startedGuessing=True
            currentGuessAlternateOptions = guess(sudoku,unusedGroup,unknownPointsGroup,unknownPoints,badGuess,guessedKeys,unguessedValues,currentGuessAlternateOptions)
            
        lastCount=len(unknownPoints)
        
        for i in range(len(sudoku)):
            for j in range(len(sudoku[0])):
                current=sudoku[i][j]
                if sudoku[i][j] == 0:
                    rowOptions=getUnusedInRow(sudoku,rows,i)
                    colOptions=getUnusedInCol(sudoku,cols,j)
                    boxOptions=getUnusedInBox(sudoku,boxes,i//3,j//3)
                    if rowOptions==-1 or colOptions==-1 or boxOptions==-1:
                        print "Wrong guess"
                        badGuess=True
                        break
                    
                    options=set(boxOptions).intersection(colOptions).intersection(rowOptions)

                    key=makeKey(i,j)
                    alreadyUnknownPoint=(key in unknownPoints)
                    
                    if alreadyUnknownPoint:
                        options=options.intersection(unknownPoints[key])

                    if len(options) == 0:
                        badGuess=True
                    elif len(options) == 1:
                        setPoint(sudoku,i,j,options.pop(),unusedGroup,unknownPointsGroup,unknownPoints,key)
                    else:
                        if not alreadyUnknownPoint:
                            unknownPointsInRow[i].append(key)
                            unknownPointsInCol[j].append(key)
                            unknownPointsInBox[i//3][j//3].append(key)
                        unknownPoints[key]=options
            if badGuess:
                break

        if not badGuess:
            for i in range(3):
                for j in range(3):
# May comment \/ out as it is redundant, may be quicker to do both though
                    eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInBox[i][j],unknownPoints)
                    badGuess = not eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInBox[i][j],unknownPoints)
                    if badGuess:
                        break
                if badGuess:
                        break
        if not badGuess:
            for i in range(len(sudoku)):
                eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInRow[i],unknownPoints)
                badGuess = not eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInRow[i],unknownPoints)
                if badGuess:
                        break
                
        if not badGuess:
            for i in range(len(sudoku[0])):
                eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInCol[i],unknownPoints)
                badGuess = not eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsInCol[i],unknownPoints)
                if badGuess:
                        break

        firstLoop=False


def guess(sudoku,unusedGroup,unknownPointsGroup,unknownPoints,badGuess,guessedKeys,unguessedValues,currentGuessAlternateOptions):
    key=-1
    if badGuess:
        print "BAD GUESS"

        if len(currentGuessAlternateOptions) > 0:
            key=guessedKeys[len(guessedKeys)-1]
        else:
            guessedKeys.pop()
            key=guessedKeys[len(guessedKeys)-1]
            currentGuessAlternateOptions=unguessedValues[key]
            
        rowCol=decodeKey(key)
        wrongValue=sudoku[rowCol[0]][rowCol[1]]
        unsetPoint(sudoku,rowCol[0],rowCol[1],wrongValue,unusedGroup,unknownPointsGroup,unknownPoints,key,currentGuessAlternateOptions.copy())
    else:               
        for possibleKey in unknownPoints.keys():
            if possibleKey not in guessedKeys:
                key=possibleKey
                break
        guessedKeys.append(key)
        currentGuessAlternateOptions=unknownPoints[key].copy()
    guess = currentGuessAlternateOptions.pop()
    unguessedValues[key]=currentGuessAlternateOptions
    rowCol=decodeKey(key)
    
    setPoint(sudoku,rowCol[0],rowCol[1],guess,unusedGroup,unknownPointsGroup,unknownPoints,key)

    return currentGuessAlternateOptions
    
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
        if len(unknownPoints[key]) == 0:
            return False
        setPoint(sudoku,rowCol[0],rowCol[1],unknownPoints[key].pop(),unusedGroup,unknownPointsGroup,unknownPoints,key)
        return True
    
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
        if len(unknownPoints[key]) == 0:
            return False
        elif len(unknownPoints[key]) == 1:
            rowCol=decodeKey(key)
            setPoint(sudoku,rowCol[0],rowCol[1],unknownPoints[key].pop(),unusedGroup,unknownPointsGroup,unknownPoints,key)

    return True
            
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

def unsetPoint(sudoku,row,col,value,unusedGroup,unknownPointsGroup,unknownPoints,key,options):
#    print "Make:",row,col,"to",value
    sudoku[row][col]=0

    unusedGroup[Group.ROW.value][row].append(value)
    unusedGroup[Group.COL.value][col].append(value)
    unusedGroup[Group.BOX.value][row//3][col//3].append(value)

    unknownPointsGroup[Group.ROW.value][row].append(key)
    unknownPointsGroup[Group.COL.value][col].append(key)
    unknownPointsGroup[Group.BOX.value][row//3][col//3].append(key)

    valueSet=set([value])
    unknownPoints[key]=options

    for key in unknownPointsGroup[Group.ROW.value][row]:
        unknownPoints[key]=unknownPoints[key].union(valueSet)
        
    for key in unknownPointsGroup[Group.COL.value][col]:
        unknownPoints[key]=unknownPoints[key].union(valueSet)
        
    for key in unknownPointsGroup[Group.BOX.value][row//3][col//3]:
        unknownPoints[key]=unknownPoints[key].union(valueSet)

def removeOptions(sudoku,row,col,options,unusedGroup,unknownPointsGroup,unknownPoints,key):    
    unknownPoints[key]=unknownPoints[key].difference(options)
                
def getUnusedInRow(sudoku,rows,row):
    if len(rows[row]) > 0:
        return rows[row]

    notInRow=[1,2,3,4,5,6,7,8,9]

    for i in range(len(sudoku[0])):
        current=sudoku[row][i]
        if current <> 0:
            if current not in notInRow:
                return -1
            else:
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
            if current not in notInCol:
                return -1
            else:
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
                if current not in notInBox:
                    return -1
                else:
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
    print ""
    for i in range(len(sudoku)):
        print sudoku[i]
    print ""

def validSudoku(sudoku):
    valid=True

    rows=[[],[],[],[],[],[],[],[],[]]
    for i in range(len(sudoku)):
        valid &= len(getUnusedInRow(sudoku,rows,i))<>-1

    cols=[[],[],[],[],[],[],[],[],[]]
    for i in range(len(sudoku[0])):
        valid &= len(getUnusedInCol(sudoku,cols,i))<>-1

    boxes=[[[],[],[]],[[],[],[]],[[],[],[]]]
    for i in range(3):
        for j in range(3):
            valid &= len(getUnusedInBox(sudoku,boxes,i,j))<>-1

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

#    print "Before:"
 #   printSudoku(sudoku)
    solveSudoku(sudoku)
#    print "After:"
#    printSudoku(sudoku)

    print "Valid:",validSudoku(sudoku)

    sumOfTopLeft+= 100 * sudoku[0][0] + 10 * sudoku[0][1] + sudoku[0][2]
    line=sudokuFile.readline()

print "Result: ",sumOfTopLeft
