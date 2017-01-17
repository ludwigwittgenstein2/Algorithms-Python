# -*- coding: utf-8 -*-

"""
# Author: Rick Sam
# Book: Algorithms for Python
# Date: Septmber 29, 2016
# Title: Recursive Selection Sort
"""

def sel_sort_rect(seq, i):
    '''Function for Recursive Selection Sort.
    '''
    if i == 0:
        return
    max_j=i
    for j in range(i):
        if seq[j] > seq[max_j]:
            max_j=j
    seq[i], seq[max_j]=seq[max_j], seq[i]
    sel_sort_rect(seq,i-1)


if __name__ == '__main__':
    seq = [10,9,8]
    print sel_sort_rect(seq, 2)
