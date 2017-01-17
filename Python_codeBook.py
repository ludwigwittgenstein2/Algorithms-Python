import random
import math

def gcd_denominator(a,b):
    '''Implements GCD denominator.'''
    while b!=0:
        result = b
        a,b = b,a%b
    return result

def test_random():
    values = [1,2,3,4,5]
    print random.choice(values)
    print random.choice(values)
    random.shuffle(values)
    print values

def find_fibonacci(n):
    if n < 2:
        print "This is if n<2:",n
        return n
    print "This is before fibonacci", n-1
    print "This is fibonacci n-2", n-2

    return find_fibonacci(n-1) + find_fibonacci(n-2)


def main():
    test_random()
    find_fibonacci(10)

if __name__ == '__main__':
    main()

