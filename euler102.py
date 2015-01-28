"""
Define several layers of elimination:

1. Checks based on quadrants:

Cannot contain the origin if:
-All points are in the same quadrant 
-All x values or all y values have the same sign (2 in set, diff <> 2)
(& one of the points is not the origin)

Can contain the origin if  one or more points are on the boundary:
-Check for line through origin abs(quadA-quadB)==2 (where both are boundaries (x.5))
-Point is on boundary opposite 2 quadrant points

Not sure if all of above methods = saving time, but implemeneted up to here.
Need line equation/x-intercept method,& dot component method

If in 3 quadrants or 2 opposite qudarants:

2. Must cross all 4 quadrant borders:
-Find equation of line and figure if any boundaries are within segment

3. Alternatively, use commonly used dot component method
"""

def quadrant(x,y):
    xZero=x == 0
    yZero=y == 0
    
    if xZero or yZero:
        if xZero and yZero:
            return 0.0
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
            return 1.0
        return 4.0
    elif y > 0:
        return 2.0

    return 3.0


count=0
trianglesFile = open("p102_triangles.txt")

for line in trianglesFile:
    nums=line.rstrip().split(",")
    points=[]
    quadrants=[]
    quadrantSet=[]
    boundary=0
    for i in range(0,len(nums),2):
        points.append([int(nums[i]),int(nums[i+1])])
        quad=quadrant(points[i//2][0],points[i//2][1])
        if quad == 0:
            count+=1
            break
        if not quad.is_integer():
            boundary+=1
        quadrants.append(quad)
        if quad not in quadrantSet:
            quadrantSet.append(quad)
        
    if len(quadrants) < 3:
        continue

    if len(quadrantSet)==1 or (boundary<2 and len(quadrantSet)==2 and abs(quadrantSet[0]-quadrantSet[1])<>2):
        continue

    lastCount=count
    if boundary <> 0:
        if boundary == 2:
            last=-1
            for num in quadrants:
                if not num.is_integer():
                    if last == -1:
                        last = num
                    else:
                        if abs(last-num)==2:
                            count+=1
                            break
        else:
            boundaryVal=-1
            for i in len(quadrantSet):
                if not quadrantSet[i].is_integer():
                    boundaryVal=i
                    break
            boundaryVal=quadrantSet.remove(boundaryVal)
            found=True
            for num in quadrantSet:
                diff=abs(num-boundaryVal)
                if diff == 0.5 or diff == 3.5:
                    found=False
                    break
            if found:
                count+=1
                
    if count <> lastCount:
        continue
                               

