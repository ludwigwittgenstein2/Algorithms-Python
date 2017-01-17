#!/bin/Python

"""
A Script to find out your name from random list
"""

import string
import random
import time

def find_Text():
        possibleCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits + ',;+'
        ask = input("Enter the text:\n")
        attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(ask)))
        attemptNext = ''

        generation = 0

        condition = False

        while condition == False:
                print attemptThis
                attemptNext = ''
                condition = True
                for i in range(len(ask)):
                        if attemptThis[i] != ask[i]:
                                condition = False
                                attemptNext += random.choice(possibleCharacters)
                        else:
                                attemptNext += ask[i]
                generation += 1
                attemptThis = attemptNext
                time.sleep(0.1)

        print "Number of generations is:" + str(generation) + "generations"


def main():
        find_Text()

if __name__ == '__main__':
        main()






