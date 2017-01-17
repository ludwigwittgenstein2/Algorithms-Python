"""
Author: Rick Sam
Date : Oct 3
Comments: Insertion Sort
Example: [3,4,1,2]
"""
def insertion_sort(aList):
    print aList
    for i in range(1, len(aList)):
        tmp = aList[i]
        k = i
        while k > 0 and tmp < aList[k-1]:
            aList[k] = aList[k-1]
            k -= 1
        aList[k] = tmp
    print aList

if __name__ == '__main__':
    aList = [4,3,2,1]
    insertion_sort(aList)
