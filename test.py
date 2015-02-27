from functools import partial

def getNext(array,index):
    print array
    return index

def general(f):
    return f(8)


array=[7,6,5]
getItem=partial(getNext,array)
print "R:",general(getItem)
