from enum import Enum

class Comp(Enum):
    X = 0
    Y = 1

class Dir(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    LENGTH = 4

def A*(matrix,excludeOptions,start,goalWidth)
    closedSet = []    # The set of nodes already evaluated.
    openSet = [start]    # The set of tentative nodes to be evaluated, initially containing the start node
    came_from = []   # The map of navigated nodes.

    gScore = {}
    fScore = {}
    
    gScore[start] = matrix[start[Comp.X], start[Comp.Y]] # Cost from start along best known path.
    # Estimated total cost from start to goal through y.
    fScore[start] = gScore[start] + heuristic(start, goalWidth)
 
    while len(openSet) > 0:
        current := the node in openset having the lowest f_score[] value
        if current = goal
            return reconstruct_path(came_from, goal)
 
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

def heuristic(matrix,startX,startY,goalWidth):
    widthChange=len(matrix[0])-startX-1
    return  100 * widthChange

def reconstructPath(cameFrom,current)
    totalPath = [current]
    while current in cameFrom:
        current = cameFrom[current]
        totalPath.append(current)
    return totalPath

def equalPoints(a,b):
    return a[Comp.X]==b[Comp.X] and a[Comp.Y]==b[Comp.Y]

def options(originX,originY, width, height, exclude):
    allOptions=[]
    if originY - 1 >= 0 and not exclude[Dir.UP]:
        allOptions.append([originX,originY-1])
    if originY + 1 < height and not exclude[Dir.DOWN]:
        allOptions.append([originX,originY+1])
    if originX - 1 >= 0 and not exclude[Dir.LEFT]:
        allOptions.append([originX-1,originY])
    if originX + 1 < width and not exclude[Dir.RIGHT]:
        allOptions.append([originX+1,originY])

    return allOptions


numbersFile = open("p082_matrix.txt")

matrix=[]
minPath=-1
excludeOptions = [0] * Dir.LENGTH
exclueeOptions[Dir.LEFT]=1

for line in numbersFile:
    matrix.append(line.rstrip().split(","))

for y in range(len(matrix)):
    pathTotal=A*(matrix,excludeOptions,[0,y],len(matrix[0]))
    if minPath < 0 or pathTotal < minPath:
        minPath=pathTotal

print "Result: ",minPath
