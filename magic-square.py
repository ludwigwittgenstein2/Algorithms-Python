#!/usr/bin/env python

"""
Fill a table with 3*3 with nine distinct integers from 1 to 9
so that the sum of numbers in each row, column and corner-corner
diagonal is same

"""


def manual():

    a = int(raw_input("Enter the value for a\n"))
    b = int(raw_input("Enter the value for b\n"))
    c = int(raw_input("Enter the value for c\n"))
    d = int(raw_input("Enter the value for d\n"))
    e = int(raw_input("Enter the value for e\n"))
    f = int(raw_input("Enter the value for f\n"))

    g = int(raw_input("Enter the value for g\n"))
    h = int(raw_input("Enter the value for h\n"))
    i = int(raw_input("Enter the value for i\n"))


    result_column_1 = a+b+c
    result_column_2 = d+e+f
    result_column_3 = g+h+i

    if result_column_3 == result_column_2:
        print "magic square"

    magic_square = {'a':a, 'b':b, 'c':c,
                'd':d, 'e':e, 'f':f,
                'g':g, 'h':h, 'i':i}

def main():
    manual()

if __name__ == '__main__':
    print magic_square
    print result_column_3
