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

def aStarSearch(matrix, start, goal):
    frontier = PriorityQueue()
    cameFrom = {}
    costSoFar = {}

    costSoFar[start] = valueAtPoint(matrix,start)
    frontier.put(start, costSoFar[start])
    cameFrom[start] = None

    current=(0,0)
    while not frontier.empty():
        
        current = frontier.get()
        
        if current == goal:
            break
        
        for nextSpot in options(matrix,current):

            newCost = costSoFar[current] + valueAtPoint(matrix,nextSpot)
            
            if nextSpot not in costSoFar or newCost < costSoFar[nextSpot]:
                priority = newCost + heuristic(matrix, nextSpot,goal)
                frontier.put(nextSpot, priority)
                cameFrom[nextSpot] = current
                costSoFar[nextSpot] = newCost
    
    return costSoFar[current]

def heuristic(matrix,start,goal):
    return  100 * (abs(goal[RC.ROW.value]-start[RC.ROW.value]) + \
                   abs(goal[RC.COL.value]-start[RC.COL.value]))

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

def options(matrix, point):
    allOptions=[]
    width = len(matrix[0])
    height = len(matrix)
    if point[RC.ROW.value] - 1 >= 0:
        allOptions.append((point[RC.ROW.value] - 1,point[RC.COL.value]))
    if point[RC.ROW.value] + 1 < height:
        allOptions.append((point[RC.ROW.value] + 1,point[RC.COL.value]))
    if point[RC.COL.value] - 1 >= 0:
        allOptions.append((point[RC.ROW.value],point[RC.COL.value] - 1))
    if point[RC.COL.value] + 1 < width:
        allOptions.append((point[RC.ROW.value],point[RC.COL.value] + 1))

    return allOptions


numbersFile = open("p083_matrix.txt")

matrix=[]

for line in numbersFile:
    matrix.append(line.rstrip().split(","))

    
minPath = aStarSearch(matrix,(0,0),(len(matrix)-1,len(matrix[0])-1))

print "Result: ",minPath
