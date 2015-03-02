ones = [4,3,3,5,4,4,3,5,5,4] #0-9 words in length
teens= [3,6,6,8,8,7,7,9,8,8] #10-19 words in length
tens = [4,3,6,6,5,5,5,7,6,6] #0-90 by ten words in length
hundred=7
thousand=8
andLength=3

result=0
number=0
last=0

for i in range (1,1000+1,1):
    number=i
    if number >=1000:
        result+=ones[int(number/1000)]
        result+=thousand
        number%=1000
    if number >=100:
        result+=ones[int(number/100)]
        result+=hundred
        number%=100
        if number > 0:
            result+=andLength
    if number >=10:
        if number < 20 and number > 10:
            number-=10
            result+=teens[number]
            number=0
        else:
            result+=tens[int(number/10)]
            number%=10
    if number >0:
        result+=ones[number]
    
    #print "Number: ",i," Length: ",result-last
    #last=result
    
print "Result: ",result
        
