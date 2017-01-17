#numpy
from random import randrange
seq = [randrange(10**10) for i in range(100)] # So this is creating a list with 100 random variables
# For example, [100,105,205, 2005... until 100]
dd = float("inf") # This is converting string to float, but what's the float value of inf? It shows inf?
for x in seq: # This is taking first variable in 100
    for y in seq: # This is taking again the first variable 100
        if x == y: # Okay, now both are the same, so continue...
            continue
        d = abs(x-y) # So, abs value of (100-100) = 0
        if d <dd: # Now, 0 < inf (maybe it stores as 5252.523 something like this)
            xx, yy, dd = x,y,d # Then 100100, 100100, 00 = 100, 100, 0

print xx, yy, dd # Should print similar to my upper result.....
