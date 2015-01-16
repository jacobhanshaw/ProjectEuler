from math import log 

lineNum=1
maxLine=-1
maxValue=-1
baseExpFile = open("base_exp.txt")

for line in baseExpFile:
    nums=line.rstrip().split(",")

    base=int(nums[0])
    exp=int(nums[1])

    value=log(base)*exp
    if value > maxValue:
        maxLine=lineNum
        maxValue=value

    lineNum+=1

print "Result:",maxLine
