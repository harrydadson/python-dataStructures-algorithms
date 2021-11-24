'''
Given a string with only characters X and Y. Find the minimum number of characters to remove from the string 
such that there is no interleaving of character X and Y and all the Xs appear before any Y.

Ex: input -> YXXXYXY, remove first Y, remove last X so output -> 2 (XXXYY)
'''

def minStep(str) -> int:

    charX = 'X'
    numY = 0
    minDel = 0

    for i in range(0, len(str)):
        if charX == str[i]:
            minDel = min(numY, minDel + 1)
        else:
            numY = numY + 1

    return minDel

input = 'YXXXYXY'
print(minStep(input))