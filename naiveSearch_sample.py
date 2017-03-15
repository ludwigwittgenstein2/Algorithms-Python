#!/usr/bin/Python

"""
Naive Pattern Search V.0.1
Author: Rick Sam
Comments: Script for finding patterns
"""

def naiveSearch():
    M = raw_input("Enter the Pattern or Paragraph:\n")
    N = raw_input("Enter the Pattern that you want to search:\n")
    user_input = M.upper()
    pattern = N.upper()

    for i in range(len(user_input)):
        if len(user_input) == 0:
            break
        if user_input[i] == pattern[0]:
            print "The length of Index of User Input:"+ str(len(user_input))
            print "Pattern found at Index"+ str(i)
        if user_input[i] != pattern[0]:
            print "Not Found"

    for j in range(len(pattern)):
        if len(pattern) == 0:
            break
        if pattern[j] == user_input[0]:
            print "Pattern found at Index"+ str(j)
        if pattern[j] != user_input[0]:
            print "Not Found"

def main():
    naiveSearch()

if __name__ == '__main__':
    main()

