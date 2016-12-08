#!/bin/Python
"""
Prototype for Evolution of Text

"""
import random
import time
import string

#Gathers string from lowercase, uppercase, digits and also the final
possibleCharacters = string.ascii_lowercase + string.digits+ string.ascii_uppercase+ '.,!?;:'


#Gets input for the target user
target = input("Enter your target text:")
#empty and join
attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
attempptNext = ''

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
