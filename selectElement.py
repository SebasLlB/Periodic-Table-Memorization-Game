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

def printSymbol(atomicNumber):
    for group in periodicTable:
        for element in periodicTable[group]:
            if element == atomicNumber:
                for row in periodicTable[group][element]["symbol"]:
                    print(row)

##This part goes through each element randomly and pulls out their symbol
##Chosen elements list gets smaller as each element is retrieved, until there are no more elements left
def askQuestions():
        ## First, we get a random index for chosenElements[]
        randomIndex = random.randint(0,len(chosenElements)-1)

        ## Next, we print the block
        print("\n* - - - - - - *\n")
        printSymbol(chosenElements[randomIndex])
        print("\n* - - - - - - *\n")
            
        userANumber = input("What's the Atomic Number? ")

        userEName = input("What's the element's name? ")
        userEName = userEName.lower()
        
        userEGroup = input("What group do they belong? ")
        userEGroup = userEGroup.lower().replace(" ","")

        print(userEName + ", " + userEGroup + ", " + userANumber)            
            
        del chosenElements[randomIndex]

def checkQuestions():
    ANCorrect = False
    ENCorrect = False
    EGCorrect = False

    