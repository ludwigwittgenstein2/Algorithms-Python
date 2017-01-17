"""Author:Rick Sam
    Date: Oct 10, 2016
    Comments: Basic Sequential search"""

def seq_search(aList, item):
    pos = 0
    found = False 

    while len(aList) > pos and not found:
        if aList[pos] == item:
            found = True
            print aList[pos]
        else: 
            pos = pos + 1
    return found
def main():
    aList = [10,5,6,2,5]
    item = 2
    print seq_search(aList, item)
    print seq_search([20,10,5,10], 10)
if __name__ == '__main__':
    main()
