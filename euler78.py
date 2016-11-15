#Basically copied. Needed Wikipedia and code to learn it.
#Now see that trick would be realizing pentagonal pattern in wiki equation
#and knowing how to generate the pos/neg inputs to to the pentagonal equation

p = []
p.append(1)
            
n = 1;            
while True:
    i = 0
    pentagonal = 1
    p.append(0)

    while (pentagonal <= n):                   
        sign = -1 if (i % 4 > 1) else 1
        p[n] += sign * p[n - pentagonal]
        p[n] %= 1000000
        i+=1
                 
        j = (i // 2 + 1 ) if (i % 2 == 0) else -(i // 2 + 1)
        pentagonal = j * (3 * j - 1) / 2;
    
                
    if (p[n] == 0):
        break
    n+=1

print "Result",n
