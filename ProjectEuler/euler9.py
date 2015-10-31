
power=2
goalSum=1000

found=False
goalSquare=0

for c in range(goalSum-2,0,-1):
    goalSquare=c**power
    
    for b in range(goalSum-c-1,0,-1):

        a=goalSum-c-b

        if (a**power + b**power)==goalSquare:
            print "A: ",a," B: ",b," C: ",c
            print "Goal: ",(a*b*c)
            found=True
            break
        
    if found:
        break

            
'''
c > 0
c^2-b^2=a^2
a=1000-(b+c)

500k=m^2+mn
'''
