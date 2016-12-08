"""Author: Rick Sam
    Date: Oct 16, 2016
    Comments: Recursive functions"""


def recursionFact(n):
    print "Factorial has been called with n:" + str(n)
    if n == 1:
        return n
    else:
       aValue = n * recursionFact(n-1)
       print ("Intermediate Value for ", n ," * factorial(",n-1,"):",aValue)
       return aValue
print recursionFact(10)

def fiboNumbers(k):
    if k == 0:
        return k
    elif k ==1:
        return k
    else:
        return fiboNumbers(k-1)+fiboNumbers(k-2)
print fiboNumbers(5)

def main():
    fiboNumbers(5)

if __name__ == '__main__':
    main()

