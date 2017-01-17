""" Author:Rick Sam
    Book: Algorithms Python
    Date: September 28, 2016
    Comments: I'm glad to know Sovereign love of God, We talk about God is Love, yet Are you
    experiencing it?
"""
def is_prime(n):
    print "The number is:", n
    for i in range(2, n):
        print "the number in range is:", n
        if n % i == 0:
            print "This is inner loop", n
            return False
            print "This is after return", n
    print "The number in the outer loop after running", n
    return True


if __name__ == '__main__':
    print is_prime(5)
