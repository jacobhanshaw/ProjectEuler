def binarySearchArray(array,goal):
    low=0
    high=len(array)-1
    while low<=high:
        mid=(high+low)//2
        current=array[mid]
        if goal < current:
            high=mid-1
        elif goal > current:
            low=mid+1
        else:
            return mid

    return -1

test=[1,3,5,6,7,8,9,10,11,15,20]
print binarySearchArray(test,-20)
print binarySearchArray(test,1)
print binarySearchArray(test,5)
print binarySearchArray(test,10)
print binarySearchArray(test,20)
print binarySearchArray(test,30)
