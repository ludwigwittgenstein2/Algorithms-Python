"""Author: Rick SAm
    Date: Oct 8,2018
    Comments: Started Using VIM"""

def additionRecurse(theList):
    theSum = 0
    for i in theList:
        theSum = theSum + i
    return theSum

def main():
    print additionRecurse([10,20,30,40,50,60])

if __name__ == '__main__':
    main()

