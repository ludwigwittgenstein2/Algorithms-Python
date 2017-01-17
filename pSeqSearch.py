def sequentialSearch(alist, item):
        pos = 0
        found = False

        while pos < len(alist) and not found:
                if alist[pos] == item:
                        found = True
                else:
                        pos = pos+1
        return found

testlist = [1,23,5,6,325,23,0]
print(sequentialSearch(testlist,3))

