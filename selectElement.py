from ptHashmap import periodicTable
import random

## This is where selected groups and their corresponding elements are stored
chosenElements = []

## Goes through every Periodic Table group name and see if it
## matches with the chosen groups list (userGroups) from the user.
## If so, then retrieve all elements inside said groups and place
## them inside chosenElements[]
def chooseElements(userGroups):
    for group in periodicTable:
        for chGroup in userGroups:
            if group.lower() == chGroup:
                for element in periodicTable[group]:
                    chosenElements.append(element)
    print("All elements we'll use, please check!")
    print(chosenElements) 

##This part goes through each element randomly and pulls out their symbol
##Chosen elements list gets smaller as each element is retrieved, until there are no more elements left
while len(chosenElements) > 0:
    print(chosenElements)

    randomIndex = random.randint(0,len(chosenElements)-1)
    print("index: " + str(randomIndex))
    print("Chosen element: " + str(chosenElements[randomIndex]))

    for group in periodicTable:
        for atomicN in periodicTable[group]:
            if atomicN == chosenElements[randomIndex]:
                for row in periodicTable[group][atomicN]["symbol"]:
                    print(row)
    print()
    
    del chosenElements[randomIndex]
