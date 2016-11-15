from functools import partial

def itemForIndex(index):
    if index % 2 == 0:
        return 67

    return 55

def getItem(f,array,index):
    while index >= len(array):
        array.append(f(len(array)))

    return array[index]

def floydCycle(f,x0):
    
    tortoise = f(x0)
    hare = f(tortoise)
    
    while tortoise <> hare:
        hare = f(f(hare))
        tortoise = f(tortoise)
    
    mu = 0
    tortoise = x0
    while tortoise <> hare:
        hare = f(hare)
        tortoise = f(tortoise)

        mu += 1

    lam = 1
    hare = f(tortoise)
    while tortoise <> hare:
        hare = f(hare)
        lam +=1

    return lam, mu

def floydCycleIndexed(f):
    tortoiseIndex = 1
    hareIndex = 2

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

        mu += 1

    lam = 1
    hareIndex = tortoiseIndex+1
    hare = f(hareIndex)
    while tortoise <> hare:
        hareIndex += 1
        hare = f(hareIndex)
        lam +=1

    return lam, mu

array = [23,38,67,55,67,55,67,55]
specificGetItem = partial(getItem,itemForIndex,array)

print floydCycle(specificGetItem)
