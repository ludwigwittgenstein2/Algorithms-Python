"""Author: Rick Sam
    Date: Oct 11, 2016"""

def selectionSort(aList):
    for i in range(len(aList)):
            least = i
            for k in range(i+1, len(aList)):
                if aList[i] > aList[k]:
                    least = k
            swap(aList, least, i)
def swap(something, x, y):
    tmp = something[x]
    something[x] = something[y]
    something[y] = tmp


aList = [2,5,6,9,11]
selectionSort(aList)
print aList

