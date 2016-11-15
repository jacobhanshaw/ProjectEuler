import timeit

def method0(maxVal):
    result = 0
    term0 = 1
    term1 = 1
    while term1 <= maxVal:
        if term1 % 2 == 0:
            result += term1
        term1 += term0
        term0 = term1 - term0
            
    return result

def method1(maxVal):
    a = 2
    b = 8
    c = 34
    result = a+b
    while c <= maxVal:
        result += c
        a = b
        b = c
        c = 4 * b + a
        
    return result

execs = 100000
maxVal = 4000000

tm0 = timeit.Timer("method0("+str(maxVal)+")",setup="from __main__ import method0")
tm1 = timeit.Timer("method1("+str(maxVal)+")",setup="from __main__ import method1")

print "Result:",method0(maxVal)
print "Method 0:",min(tm0.repeat(number=execs))/execs
print "Result:",method1(maxVal)
print "Method 1:",min(tm1.repeat(number=execs))/execs
