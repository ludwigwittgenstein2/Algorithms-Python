#!/bin/Python

"""
Prototype for Evolution in text to find Target text from a String
Program for Sanjay :D

"""


import random
import string
import time

possibleCharacters = string.ascii_lowercase + string.digits+ string.ascii_uppercase + '.,;!:'


#Get input from target user

target = input("Enter your target text to search:")

attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
# So this will have a string of len(input) from the user
# attemptNext will have empty string
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
                        print attemptNext
                else:
                        attemptNext += target[i]
        generation += 1
        attemptThis = attemptNext
        print "This is ", attemptThis, attemptNext
        time.sleep(0.1)

print ("Target Matched! That took" + str(generation) + "generation(s)")

