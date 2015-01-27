"""
Define several layers of elimination

1. Checks based on quadrants:

Cannot contain the origin if:
-All points are in the same quadrant 
-All x values or all y values have the same sign (2 in set, diff <> 2)
(& one of the points is not the origin)
(If multiple points, not in a quadrant then skip this test)
"""

def quadrant(x,y):
    if x == 0 or y == 0:
        return -1
    elif x > 0:
        if y > 0:
            return 1
        return 4
    elif y > 0:
        return 2

    return 3



trianglesFile = open("p102_triangles.txt")

for line in trianglesFile:
    nums=line.rstrip().split(",")
    points=[]
    for i in range(0,len(nums),2):
        points.append([int(nums[i]),int(nums[i+1])])
    print points
