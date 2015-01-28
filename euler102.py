"""
Define several layers of elimination:

1. Checks based on quadrants:

Cannot contain the origin if:
-All points are in the same quadrant 
-All x values or all y values have the same sign (2 in set, diff <> 2)
(& one of the points is not the origin)
(If multiple points, not in a quadrant then skip this test)

If in 3 quadrants, 2 opposite qudarants, 

2. Must cross all 4 quadrant borders or line segment through origin:

"""

def quadrant(x,y):
    xZero=x == 0
    yZero=y == 0
    
    if xZero or yZero:
        if xZero and yZero:
            return 0
        elif xZero:
            if y > 0:
                return 1.5
            else:
                return 3.5
        else:
            if x > 0:
                return 4.5
            else:
                2.5
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
