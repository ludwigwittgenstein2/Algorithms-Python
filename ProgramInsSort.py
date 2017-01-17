"""Author:Rick Sam
    Oct 14, 2016
    Insertion Sort"""

def ins_Sort(item):
    for i in range(1,len(item)):
        j = i
        while j > 0 and item[j] < item[j-1]:
            item[j], item[j-1] = item[j-1], item[j]
            j -= 1
    print item

item = [5,4,3,2,1]
ins_Sort(item)


