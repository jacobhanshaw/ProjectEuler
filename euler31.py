goal=200
options=[1,2,5,10,20,50,100,200]

optionsByFive=[5,10,20,50,100,200]
otherOptions=[1,2]
    
c=[0]*(goal+1)
c[0]=1

#for  multiples of 5
for k in optionsByFive:
    for i in range(0,goal-k+1,5):
        c[i+k]+=c[i]
        
#for the rest
for k in otherOptions:
    for i in range(0,goal-k+1,1):
        c[i+k]+=c[i]
        
print "Result: ",c[goal]
