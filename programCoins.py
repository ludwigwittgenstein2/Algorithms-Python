#-*- coding:utf -8-*-
"""
In Line 14, I understand that it is checking if an item
is in coinValueList and it should be less than 63.
After that, in Line 17 –– numCoin variable is created, 
1+ calling the same function, change-i? 
So it means 63 - 1? And, so totally it will have 1+62?
What does numCoins have?

recursive functions like that can be hard to wrap your mind around.
"So it means 63 - 1? And, so totally it will have 1+62?"
Yes, that line will set numCoins to 63 and then it will check to see
if numCoins is less that minCoins(63). But that is only for the first
increment when i=1. It will then run again with i=5 and then it will again
check if the answer it gets is less than minCoins. going through each recursion checking for each value of i and then setting minCoins if it finds a lower value than any previous recursions.
"""

def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else: 
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1+ recMC(coinValueList, change-i)
    
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins
    print minCoins

print (recMC([1,5,10,25],63))
