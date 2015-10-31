import heapq
from enum import Enum

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

class RC(Enum):
    ROW=0
    COL=1

class Dir(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    LENGTH = 4

def aStarSearch(matrix, excludeOptions, startOptions, goalWidth):
    frontier = PriorityQueue()
    cameFrom = {}
    costSoFar = {}

    for start in startOptions:
        costSoFar[start] = valueAtPoint(matrix,start)
        frontier.put(start, costSoFar[start])
        cameFrom[start] = None

    current=(0,0)
    while not frontier.empty():
        
        current = frontier.get()
        
        if current[RC.COL.value] == goalWidth:
            break
        
        for nextSpot in options(matrix,current,excludeOptions):

            newCost = costSoFar[current] + valueAtPoint(matrix,nextSpot)
            
            if nextSpot not in costSoFar or newCost < costSoFar[nextSpot]:
                priority = newCost + heuristic(matrix, nextSpot,goalWidth)
                frontier.put(nextSpot, priority)
                cameFrom[nextSpot] = current
                costSoFar[nextSpot] = newCost
    
    return costSoFar[current]

def heuristic(matrix,start,goalWidth):
    widthChange=len(matrix[0])-start[RC.COL.value]
    return  100 * widthChange

def valueAtPoint(matrix,point):
    return int(matrix[point[RC.ROW.value]][point[RC.COL.value]])

def reconstructPath(current,cameFrom):
    totalPath = [current]
    while current is not None:
        current = cameFrom[current]
        totalPath.append(current)
    return totalPath

def equalPoints(a,b):
    return a[RC.ROW.value]==b[RC.ROW.value] and a[RC.COL.value]==b[RC.COL.value]

def options(matrix, point, exclude):
    allOptions=[]
    width = len(matrix[0])
    height = len(matrix)
    if point[RC.ROW.value] - 1 >= 0 and not exclude[Dir.UP.value]:
        allOptions.append((point[RC.ROW.value] - 1,point[RC.COL.value]))
    if point[RC.ROW.value] + 1 < height and not exclude[Dir.DOWN.value]:
        allOptions.append((point[RC.ROW.value] + 1,point[RC.COL.value]))
    if point[RC.COL.value] - 1 >= 0 and not exclude[Dir.LEFT.value]:
        allOptions.append((point[RC.ROW.value],point[RC.COL.value] - 1))
    if point[RC.COL.value] + 1 < width and not exclude[Dir.RIGHT.value]:
        allOptions.append((point[RC.ROW.value],point[RC.COL.value] + 1))

    return allOptions


numbersFile = open("p082_matrix.txt")

matrix=[]
excludeOptions = [0] * Dir.LENGTH.value
excludeOptions[Dir.LEFT.value]=1

for line in numbersFile:
    matrix.append(line.rstrip().split(","))

startOptions=[]
for r in range(len(matrix)):
    startOptions.append((r,0))
    
minPath = aStarSearch(matrix,excludeOptions,startOptions,len(matrix[0])-1)

print "Result: ",minPath
