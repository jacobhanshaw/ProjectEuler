from enum import Enum
from Queue import PriorityQueue

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
            
    def toString(self):
        return "({0}, {1})".format(self.x, self.y)

class Dir(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    LENGTH = 4

def aStarSearch(matrix, excludeOptions, start, goalWidth):
    frontier = PriorityQueue()
    frontier.put(start, valueAtPoint(matrix,start))
    cameFrom = {}
    costSoFar = {}
    cameFrom[start] = None
    costSoFar[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current.x == goalWidth:
            break
        
        for nextSpot in options(matrix,current,excludeOptions):

            newCost = costSoFar[current] + valueAtPoint(matrix,nextSpot)
            if nextSpot not in costSoFar or newCost < costSoFar[nextSpot]:
                costSoFar[nextSpot] = newCost
                priority = newCost + heuristic(matrix, nextSpot,goalWidth)
                frontier.put(nextSpot, priority)
                cameFrom[nextSpot] = current
    
    return costSoFar
"""
def A*(matrix,excludeOptions,start,goalWidth)
    closedSet = []    # The set of nodes already evaluated.
    openSet = [start]    # The set of tentative nodes to be evaluated, initially containing the start node
    cameFrom = {}   # The map of navigated nodes.

    gScore = {}
    fScore = {}
    
    gScore[start] = matrix[start[Comp.X], start[Comp.Y]] # Cost from start along best known path.
    # Estimated total cost from start to goal through y.
    fScore[start] = gScore[start] + heuristic(start, goalWidth)
 
    while len(openSet) > 0:
        current = the node in openset having the lowest f_score[] value
        if equalPoints(current,goal):
            return reconstructPath(cameFrom, goal)
 
        remove current from openset
        add current to closedset
        for each neighbor in neighbor_nodes(current)
            if neighbor in closedset
                continue
            tentative_g_score := g_score[current] + dist_between(current,neighbor)
 
            if neighbor not in openset or tentative_g_score < g_score[neighbor] 
                came_from[neighbor] := current
                g_score[neighbor] := tentative_g_score
                f_score[neighbor] := g_score[neighbor] + heuristic_cost_estimate(neighbor, goal)
                if neighbor not in openset
                    add neighbor to openset
 
    return []
"""
def heuristic(matrix,start,goalWidth):
    widthChange=len(matrix[0])-start.x
    return  100 * widthChange

def valueAtPoint(matrix,point):
    return int(matrix[point.x][point.y])

def reconstructPath(cameFrom,current):
    totalPath = [current]
    while current in cameFrom:
        current = cameFrom[current]
        totalPath.append(current)
    return totalPath

def equalPoints(a,b):
    return a.x==b.x and a.y==b.y

def options(matrix, point, exclude):
    allOptions=[]
    width = len(matrix[0])
    height = len(matrix)
    if point.y - 1 >= 0 and not exclude[Dir.UP.value]:
        allOptions.append(Point(point.x,point.y-1))
    if point.y + 1 < height and not exclude[Dir.DOWN.value]:
        allOptions.append(Point(point.x,point.y+1))
    if point.x - 1 >= 0 and not exclude[Dir.LEFT.value]:
        allOptions.append(Point(point.x-1,point.y))
    if point.x + 1 < width and not exclude[Dir.RIGHT.value]:
        allOptions.append(Point(point.x+1,point.y))

    return allOptions


numbersFile = open("p082_matrix.txt")

matrix=[]
minPath=-1
excludeOptions = [0] * Dir.LENGTH.value
excludeOptions[Dir.LEFT.value]=1

for line in numbersFile:
    matrix.append(line.rstrip().split(","))

for y in range(len(matrix)):
    pathTotal=aStarSearch(matrix,excludeOptions,Point(0,y),len(matrix[0]))
    if minPath < 0 or pathTotal < minPath:
        minPath=pathTotal

print "Result: ",minPath
