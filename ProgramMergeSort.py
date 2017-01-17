"""Author:Rick Sam
    Oct 14, 2016
    Comments: Catching up on algorithms"""
def merge_sort(item):
    '''Merge Sort function.'''
    if len(item) > 1:
        mid = len(item)/2
        left = item[0:mid]
        right = item[mid::]
    
        merge_sort(left)
        merge_sort(right)
        print "This is divison of left:", merge_sort(left)
        print "This is divison of rght.", merge_sort(right)

        l, r = 0, 0

        for i in range(len(item)):
            if l < len(left):
                lval = left[l]
            else:
                None
            if r < len(right):
                rval = right[r]
            else:
                None
            if (lval and rval and lval < rval) or rval is None:
                item[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or lval is None:
                item[i]=rval
                r += 1
            else:
                raise Exception("Could not merge, sub arrays")
    print item

def main():
    item = [10,9,8,7,6,5,4,3]
    merge_sort(item)
if __name__ == '__main__':
    main()

