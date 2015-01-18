goal=100
    
c=[0]*(goal+1)
c[0]=1

for k in range(1,goal):
    for i in range(0,goal-k+1,1):
        c[i+k]+=c[i]
        
print "Result: ",c[goal]
