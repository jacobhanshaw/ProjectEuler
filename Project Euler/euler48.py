result=0

for i in range(1,1000,1):
    result+=i**i

strResult=str(result)
print "Result: ",strResult[len(strResult)-10:len(strResult)]
