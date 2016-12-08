"""Author: Rick Sam
    Date: Oct 8, 2016
    Comments: Just starting to use Vim"""

def additionRecursion(theList):
    theSum = 0
    for i in theList:
        theSum = theSum+i
    return theSum
print additionRecursion([1,2,3,4,5])

