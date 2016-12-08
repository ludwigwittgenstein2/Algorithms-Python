
def insertion_sort(aList):
        for i in range(1,len(aList)):
                j = i
                while j > 0 and aList[j-1] > aList[j]:
                        aList[j-1],aList[j] = aList[j], aList[j-1]
                        j -=1
        return aList

aList=[10,9,5,4,2,1]
insertion_sort(aList)
print aList
