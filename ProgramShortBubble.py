"""Author: Rick Sam
    Date: Oct 11, 2016"""

def ProgramShortBubble(aList):
    name = True
    passnum = len(aList) - 1
    while passnum > 0 and name: 
        name = False
        for i in range(passnum):
            if aList[i]>aList[i+1]:
               name = True 
               temp = aList[i]
               aList[i] = aList[i+1]
               aList[i+1] = temp
        passnum = passnum-1

aList= [20,15, 1, 2, 80, 30, 15]
ProgramShortBubble(aList)
print aList

