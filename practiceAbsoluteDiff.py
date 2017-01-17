# -*- coding: utf-8 -*-
""" Author: Rick Sam
    Date : September 26
    Program: To find the numbers with absolute differences, meaning two numbers
    who are close to each other
    Comments: Frustrated that I can't understand details in asymptotic analysis.
    Read Psalm 53, today –– It seems that there's pretty much everything needed to continue
    Life. And the Psalmist understand the deep needs of human emotions.
    How to solve this? : Given a list, what I can do is find which number has the smallest absolute difference
    and print them out? Sounds fair, right?
"""
from random import randrange
seq = [randrange(10) for i in range(10)]
print seq
dd = float("inf")
for number in seq:
    for value in seq:
        if number == value:
            continue
        d = abs(number - value)
        if d < dd:
            number, value, d = number, value, d

print number, value, d
