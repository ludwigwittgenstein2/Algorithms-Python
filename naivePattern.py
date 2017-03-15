#!/usr/bin/Python

"""
Naive Pattern Search
txt[] = "This is a TEST"
pat[] = "Test"

Pattern found at index [x]
Author: Rick Sam

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

def naivePatternTwo(given_input, pattern_to_search):
    M = len(given_input)
    N = len(pattern_to_search)

    for i in range(M):
        for j in range(N):
            if given_input[i+j] != pattern_to_search[j]:
                break
            else:
                print "Found"
        if pattern_to_search[j] == given_input[i]:
            print "Pattern"

def naiveBookSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    for i in xrange(N-M+1):
        print "This is i:", i
        for j in xrange(M):
            print "this is j:", j
            print "this is txt[i+j]", txt[i+j]
            print "This is pat[j]:", pat[j]
            if txt[i+j] != pat[j]:
                print "Text", txt[i+j]
                break
        if j == M-1:
            print "This is J", j
            print "Pattern found at index" + str(i), str(j)

def main():
    naive_pattern()
#   given_input = "ABSASFAGDGDS"
#   pattern_to_search = "AB"
#   naivePatternTwo(given_input, pattern_to_search)
#   txt = "AAABBB"
#   pat = "BB"
#   naiveBookSearch(pat, txt)

if __name__ =='__main__':
    main()
