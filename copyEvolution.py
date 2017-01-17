#!/bin/Python

"""
A small script to find your name or text,
Generation means the number of loops to find your text
Enjoy

"""

import random
import string
import time

generation = 0

def Evolution():
#Gathers string from lowercase, uppercase, digits and also the final
        possibleCharacters = string.ascii_lowercase + string.digits+ string.ascii_uppercase+ '.,!?;:'


#Gets input for the target user
        target = input("Enter your target text:")
#empty and join
        attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
        attemptNext = ''

        completed = False

        generation = 0

        while completed == False:
                print attemptThis
                attemptNext = ''
                completed = True
                for i in range(len(target)):
                        if attemptThis[i] != target[i]:
                                completed = False
                                attemptNext += random.choice(possibleCharacters)
                        else:
                                attemptNext += target[i]
                generation += 1
                attemptThis = attemptNext
                time.sleep(0.1)

        print ("Target Matched! That took"+ str(generation) + "generation(s)")

def main():
        Evolution()

