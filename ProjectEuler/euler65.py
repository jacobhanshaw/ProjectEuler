
Am2=8
Am1=11

Bm2=3
Bm1=4

i=5
goal=100

lastB=2

while i <= goal:
    b=1
    if i % 3 == 0:
        lastB+=2
        b=lastB
    A=b*Am1+Am2
    B=b*Bm1+Bm2
    if i == goal:
        result=0
        strA=str(A)
        for j in range(len(strA)):
            result+=int(strA[j])
        print "Result:",result
    else:
        Am2=Am1
        Am1=A
        Bm2=Bm1
        Bm1=B

    i+=1
