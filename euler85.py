goal=2000000

startSize=1
endSize=2000

minDiff=-1
rHeight=-1
rWidth=-1

for width in range(startSize,endSize+1):
    for height in range(width,endSize+1):
        squares=((width * (width+1))/2)*((height * (height+1))/2)
        diff=abs(goal-squares)
        if minDiff==-1 or diff < minDiff:
            minDiff=diff
            rHeight=height
            rWidth=width

print rHeight,"X",rWidth,"=",(rHeight*rWidth),"Diff:",minDiff
