from ptHashmap import periodicTable
from ptPrinting import printPeriodic
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
                abbr = periodicTable[group][element]["abbr"]
                for row in periodicTable[group][element]["symbol"]:
                    print(row)
    return abbr

def checkQuestions(userEN, userEG, atomicNumber):
    ENCorrect = False
    EGCorrect = False

    for group in periodicTable:
        if group.lower().replace(" ","") == userEG:
            EGCorrect = True
        for element in periodicTable[group]:
            if element == atomicNumber:
                if periodicTable[group][element]["name"] == userEN:
                    ENCorrect = True  
                    
                
    if  ENCorrect == EGCorrect == True:
        return True
    else:
        return False

##This part goes through each element randomly and pulls out their symbol
##Chosen elements list gets smaller as each element is retrieved, until there are no more elements left
def askQuestions():
    while(len(chosenElements) > 0):
        ## First, we get a random index for chosenElements[]
        randomIndex = random.randint(0,len(chosenElements)-1)
        actualElement = chosenElements[randomIndex]

        ## Next, we print the block
        print("\n* - - - - - - *\n")
        abbreviation = printSymbol(actualElement)
        print("\n* - - - - - - *\n")
            
        userANumber = input("What's the Atomic Number? ")

        userEName = input("What's the element's name? ")
        userEName = userEName.lower()
        
        userEGroup = input("What group do they belong? ")
        userEGroup = userEGroup.lower().replace(" ","")          

        answers = checkQuestions(userEName, userEGroup, actualElement)

        if (int(userANumber) == actualElement):
            answers = answers
        else: 
            answers = False
        
        printPeriodic(answers, abbreviation, chosenElements[randomIndex])
            
        del chosenElements[randomIndex]

        
        



    