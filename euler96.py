from enum import Enum
from copy import deepcopy

#UGH A BILLION SCOPE ISSUES!
#REEEEEALLY had to come to grips with the fact that lists passed by reference could not be re-assigned to a new list
#All this needs scraped

#Would like to change to use binary logic instead.
#0 = 0
#1 = 1
#2 = 1 << 1
#3 = 1 << 2
#...
#Sets are or'd together for union, and'd for intersection, and and'd with not the number to remove.

class Group(Enum):
    ROW=0
    COL=1
    BOX=2
    LEN=3

class State:

    def __init__(self,sudoku,rows=None, cols=None, boxes=None, unknownPoints=None, \
                 unknownPointsInRow=None, unknownPointsInCol=None, unknownPointsInBox=None):
        self.sudoku = sudoku
        self.rows = rows or [[],[],[],[],[],[],[],[],[]]
        self.cols = cols or [[],[],[],[],[],[],[],[],[]]
        self.boxes = boxes or [[[],[],[]],[[],[],[]],[[],[],[]]]

        self.unknownPoints = unknownPoints or {}
        self.unknownPointsInRow = unknownPointsInRow or [[],[],[],[],[],[],[],[],[]]
        self.unknownPointsInCol = unknownPointsInCol or [[],[],[],[],[],[],[],[],[]]
        self.unknownPointsInBox = unknownPointsInBox or [[[],[],[]],[[],[],[]],[[],[],[]]]

#NEED TO TRACK ALL COMPUTER CHOICES SINCE GUESSING STARTED

def solveSudoku(sudoku):

    rows=[[],[],[],[],[],[],[],[],[]]
    cols=[[],[],[],[],[],[],[],[],[]]
    boxes=[[[],[],[]],[[],[],[]],[[],[],[]]]
    unusedGroup=[rows,cols,boxes]

    unknownPoints={}
    unknownPointsInRow=[[],[],[],[],[],[],[],[],[]]
    unknownPointsInCol=[[],[],[],[],[],[],[],[],[]]
    unknownPointsInBox=[[[],[],[]],[[],[],[]],[[],[],[]]]
    unknownPointsGroup=[unknownPointsInRow,unknownPointsInCol,unknownPointsInBox]

    lastCount=-1
    firstLoop = True

    states=[]       #Push before adding guess
    badGuess=False
    guessedKeys=[]
    unguessedValues={}
    currentGuessAlternateOptions=set([])
    
    while len(unknownPoints) or firstLoop:

 #       if badGuess:
 #           printSudoku(sudoku)

        if len(unknownPoints) == lastCount or badGuess:
            changes = guess(sudoku,states,unusedGroup,unknownPointsGroup,unknownPoints,badGuess,guessedKeys,unguessedValues,currentGuessAlternateOptions)
            sudoku = changes[0]
            unknownPoints = changes[1]
            currentGuessAlternateOptions = changes[2]
            badGuess=False


            
        lastCount=len(unknownPoints)
        
        for i in range(len(sudoku)):
            for j in range(len(sudoku[0])):
                current=sudoku[i][j]
                if sudoku[i][j] == 0:
                    rowOptions=getUnusedInRow(sudoku,unusedGroup[Group.ROW.value],i)
                    colOptions=getUnusedInCol(sudoku,unusedGroup[Group.COL.value],j)
                    boxOptions=getUnusedInBox(sudoku,unusedGroup[Group.BOX.value],i//3,j//3)
                    if rowOptions==-1 or colOptions==-1 or boxOptions==-1:
 #                       print "Intersect Wrong guess",i,j
                        badGuess=True
                        break
                    
                    options=set(boxOptions).intersection(colOptions).intersection(rowOptions)

                    key=makeKey(i,j)
                    alreadyUnknownPoint=(key in unknownPoints)
                    
                    if alreadyUnknownPoint:
                        options=options.intersection(unknownPoints[key])

                    if len(options) == 0:
 #                       print "Options wrong guess",i,j
                        badGuess=True
                        break
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
                    eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsGroup[2][i][j],unknownPoints)
                    badGuess = not eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsGroup[2][i][j],unknownPoints)
                    if badGuess:
 #                       print "BOX Wrong guess",i,j
                        break
                if badGuess:
                        break
        if not badGuess:
            for i in range(len(sudoku)):
                eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsGroup[0][i],unknownPoints)
                badGuess = not eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsGroup[0][i],unknownPoints)
                if badGuess:
 #                   print "ROW Wrong guess",i
                    break
                
        if not badGuess:
            for i in range(len(sudoku[0])):
                eliminateByOnlyPossibleInGroup(sudoku,unusedGroup,unknownPointsGroup,unknownPointsGroup[1][i],unknownPoints)
                badGuess = not eliminateByGroups(sudoku,unusedGroup,unknownPointsGroup,unknownPointsGroup[1][i],unknownPoints)
                if badGuess:
 #                   print "COL Wrong guess",j
                    break

        firstLoop=False
        
    return 100 * sudoku[0][0] + 10 * sudoku[0][1] + sudoku[0][2]


def guess(sudoku,states,unusedGroup,unknownPointsGroup,unknownPoints,badGuess,guessedKeys,unguessedValues,currentGuessAlternateOptions):
    key=-1

#    printSudoku(sudoku)
    
    if badGuess:
 #       print "BAD GUESS"
 #       print "Guessed:",guessedKeys
 #       print "Alt:",currentGuessAlternateOptions

        #Return state
        state=states.pop()
        sudoku=state.sudoku
        unusedGroup[Group.ROW.value]=state.rows
        unusedGroup[Group.COL.value]=state.cols
        unusedGroup[Group.BOX.value]=state.boxes

        unknownPoints=state.unknownPoints
        unknownPointsGroup[Group.ROW.value]=state.unknownPointsInRow
        unknownPointsGroup[Group.COL.value]=state.unknownPointsInCol
        unknownPointsGroup[Group.BOX.value]=state.unknownPointsInBox

        if len(currentGuessAlternateOptions) > 0:
            key=guessedKeys[len(guessedKeys)-1]
        else:
            guessedKeys.pop()
            key=guessedKeys[len(guessedKeys)-1]
            currentGuessAlternateOptions=unguessedValues[key]
    else:               
        for possibleKey in unknownPoints.keys():
            if possibleKey not in guessedKeys:
                key=possibleKey
                break
        guessedKeys.append(key)
        currentGuessAlternateOptions=unknownPoints[key].copy()
    
    #Set state
    state=State(deepcopy(sudoku),deepcopy(unusedGroup[Group.ROW.value]),deepcopy(unusedGroup[Group.COL.value]), deepcopy(unusedGroup[Group.BOX.value]), deepcopy(unknownPoints), \
        deepcopy(unknownPointsGroup[Group.ROW.value]), deepcopy(unknownPointsGroup[Group.COL.value]), deepcopy(unknownPointsGroup[Group.BOX.value]))
    states.append(state)
    guess = currentGuessAlternateOptions.pop()
    unguessedValues[key]=currentGuessAlternateOptions
    rowCol=decodeKey(key)

 #   print "Guessing:",guess,"for",rowCol
    
    setPoint(sudoku,rowCol[0],rowCol[1],guess,unusedGroup,unknownPointsGroup,unknownPoints,key)

    return [sudoku,unknownPoints,currentGuessAlternateOptions]
    
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
    #print "Make:",row,col,"to",value
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
    print "Unset:",row,col,"to",value
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
    sumOfTopLeft+=solveSudoku(sudoku)
#    print "After:"
#    printSudoku(sudoku)

#    print "Valid:",validSudoku(sudoku)

 #   sumOfTopLeft+= 100 * sudoku[0][0] + 10 * sudoku[0][1] + sudoku[0][2]
    line=sudokuFile.readline()

print "Result: ",sumOfTopLeft
