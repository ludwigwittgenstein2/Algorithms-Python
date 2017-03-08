#!/usr/bin/Python

"""
Naive Pattern Search
txt[] = "This is a TEST"
pat[] = "Test"

Pattern found at index [x]
Author: Rick Sam
Comments: Sunlight is precious to me, And I thank
God for it.

"""

def naive_pattern():
    user_input=raw_input("Enter the paragraph to search:\n")
    txt = user_input.upper()
    pattern_search = raw_input("Enter the Pattern you need to search:\n")
    user_value = pattern_search.upper()
    patternList = []


    for i in range(len(txt)):
        if len(txt) == 0:
            break
        if txt[i] == user_value[0]:
            print "Pattern found at index" + str([i])
    for j in range(len(user_value)):
        if len(user_value) == 0:
            break
        if user_value[j] == txt[0]:
            print "Pattern found at index" + str([j])

def main():
    naive_pattern()

if __name__ =='__main__':
    main()
