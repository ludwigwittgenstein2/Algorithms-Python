"""Author: Rick Sam
    Date: Oct 10, 2016
    Comments: Binary Search"""

def binarySearch(aList, item):
    first = 0
    last = len(aList)-1
    found = False 

    while first <= last and not found:
        mid = (first+last)//2
        if aList[mid] == item:
            found = True
        else:
            if item < aList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

aList = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print binarySearch(aList, 17)

