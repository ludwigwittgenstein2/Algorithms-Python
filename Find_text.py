#!/bin/Python

"""
A small script to find your name or text,
Generation means the number of loops to find your text
Enjoy

"""

import random
import string
import time

def Evolution():
        possibleCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits + '.;+'
        user = input("Enter the target to search:")
        thisNow = ''.join(random.choice(possibleCharacters) for i in range(len(user)))
        thisNext = ''

        data = False
        generation = 0

        while data == False:
                print thisNow
                thisNext = ''
                data = True
        for i in range(len(user)):
                if thisNow[i] != user[i]:
                        data = False
                        thisNext += random.choice(possibleCharacters)
                else:
                        thisNext += user[i]
        generation += 1
        thisNow = thisNext
        time.sleep(0.10)

        print "It took" + str(generation) + "generations."

def main():
        Evolution()


if __name__ == '__main__':
        main()






