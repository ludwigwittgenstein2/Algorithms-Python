"""
Author: Rick Sam
Book: Algorithms for Python
Comments: Recursion
"""
def T(seq, i=0):
    if i == len(seq):
        return 1
    return T(seq, i+1)+1

if __name__ == '__main__':
    seq = [10,5,2,6,4,3]
    print T(seq)
