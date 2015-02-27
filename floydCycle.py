from functools import partial

def itemForIndex(index):
    return index % 10

def getItem(f,array,index):
    while index >= len(array):
        array.append(f(len(array)))

    return array[index]

def floydCycle(f):
    tortoiseIndex = 0
    hareIndex = 1

    tortoise = f(tortoiseIndex)
    hare = f(hareIndex)
    
    while tortoise <> hare:
        
        tortoiseIndex += 1
        tortoise = f(tortoiseIndex)
        
        hareIndex += 2
        hare = f(hareIndex)

    mu = 0
    tortoiseIndex = 0
    tortoise = f(tortoiseIndex)
    while tortoise <> hare:
        tortoiseIndex += 1
        tortoise = f(tortoiseIndex)

        hareIndex += 1
        hare = f(hareIndex)

        print "T:",tortoiseIndex,tortoise
        print "H:",hareIndex,hare

        mu += 1

    lam = 1
    hareIndex = tortoiseIndex+1
    hare = f(hareIndex)
    while tortoise <> hare:
        hareIndex += 1
        hare = f(hareIndex)
        lam +=1

    return lam, mu

array = [0,1,2,3,4,5,6,7,8]
specificGetItem = partial(getItem,itemForIndex,array)

print floydCycle(specificGetItem)
