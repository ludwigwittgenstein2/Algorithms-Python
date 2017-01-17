# -*- coding: utf-8 -*-
""" Author: Rick Sam
    Date: September 29, 2016
    Title: Gnome Sort
    Comments: Trying to figure out algorithms intuitively
"""
import cProfile

def gnomesort(seq):
    i = 0
    print "Before Sorting:", seq
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
            print "This is executing", i
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
            print "Else is executing", i
    print "After Sorting:", seq


if __name__ == '__main__':
    seq = [99,55,44, 23, 15]
    gnomesort(seq)
    print cProfile.run('gnomesort')
