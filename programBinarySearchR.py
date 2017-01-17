import cProfile

def binary_search(aList, item):
        """It searches the item by divide and conquer."""
        first = 0
        last = (len(aList)-1)
        found = False
        while first <= last and not found:
                mid = (first+last)//2
                if aList[mid] == item:
                        found = True
                else:
                        if item < aList[mid]:
                                last = mid -1
                        else:
                                first = mid + 1
        return found

aList = [10,11,12,13,14,15,16]
print binary_search(aList, 15)

def search_binary(aList,item):
        ''' Binary searches by divide and conquer.'''
        first = 0
        last = (len(aList)-1)
        found = False

        while first <= last and not found:
                mid = (first+last)//2
                if aList[mid] == item:
                        found = True
                else:
                        if item < aList[mid]:
                                last = mid -1
                        else:
                                first = mid +1
        return found

def main():
        aList = [1,5,19]
        nList=search_binary(aList,5)
if __name__ == '__main__':
        main()
        cProfile.run('print main')

