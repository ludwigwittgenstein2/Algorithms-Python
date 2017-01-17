#!/bin/Python
# timing 7 different Python sorting algorithms with a list of integers
# each function is given the same list (fresh copy each time)
# tested with Python24       vegaseat      21jan2006
import random  # for generating random numbers
import time    # for timing each sort function with time.clock()
DEBUG = False  # set True to check results of each sort
N = 1000     # number of elements in list
list1 = []   # list of integer elements
for i in range(0, N):
    list1.append(random.randint(0, N-1))
#print list1  # test
def print_timing(func):
    def wrapper(*arg):
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper


def main():
        print_timing(func)

if __name__ == '__main__':
        main()
