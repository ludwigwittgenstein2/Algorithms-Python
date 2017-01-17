
def bSearch(aList, item):
    first = 0
    last = len(aList) - 1 
    found = False

    while first <= last and not found: 
        mid = (first+last)//2
        if aList[mid] == item:
            found = True
        else: 
            if item < aList[mid]:
                last = mid -1
                print last
            else:
                first = mid + 1
                print first
    return found

aList = [0,1,2,3,4,56,88]
print bSearch(aList, 88)

