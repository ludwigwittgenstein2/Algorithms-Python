"""Author:Rick Sam
    Date: Oct 30,2016
    Comments: Gnome Sort"""

def gnomeSort(aList):
    i = 0
    n = len(aList)
    while i < n:
        if aList[i] < aList[i-1]:
            aList[i],aList[i-1] = aList[i-1],aList[i]
        else:
            i = i+1

def main():
    aList=[10,9,8,5,4,3,2,100]
    gnomeSort(aList)

if __name__ == '__main__':
    main()

