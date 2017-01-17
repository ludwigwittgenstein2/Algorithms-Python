def bubble_Sort(item):
    """bubble sort"""
    for i in range(len(item)):
        for j in range(len(item)-1-i):
            if item[j] > item[j+1]:
                item[j], item[j+1] = item[j+1], item[j]
    print item
def main():
   item = [5,4,3,2,1]
   print bubble_Sort(item)

if __name__=='__main__':
    main()

