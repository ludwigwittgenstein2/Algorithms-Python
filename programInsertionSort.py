"""Author: Rick Sam
    Date: Oct 11, 2016
    Comment: Insertion Sort"""

def insertionSort(aList):
    for i in range(1, len(aList)):
        tmp = aList[i]
        k = i

        while k > 0 and aList[k] > aList[k-1]:
            print "Last list",aList[k-1]
            aList[k] = aList[k-1]
            k -= 1
        aList[k] = tmp
        print "Temprary", tmp
        print aList


aList = [1,10,9,8]
insertionSort(aList)

print insertionSort(aList)
