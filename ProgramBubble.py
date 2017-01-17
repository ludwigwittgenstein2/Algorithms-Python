"""Author: Rick Sam
    Date: Oct 11, 2016
    Comments: Not sure of Line 7,8"""


def bubbleSort(aList):
    print "Before Bubble Sort", aList
    for number in range(len(aList)-1, 0,-1):
        for j in range(number):
            if aList[j] > aList[j+1]:
                temp = aList[j]
                aList[j] = aList[j+1]
                aList[j+1] = temp

aList = [20,10,15,3,5]
bubbleSort(aList)
print aList

