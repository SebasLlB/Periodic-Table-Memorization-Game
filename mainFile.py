#Let's start setting up an example hashmap for the Alkaline Metals
from ptPrinting import printPeriodic 
from ptHashmap import periodicTable
import random

chosenElements = []
chosenGroups = ["alkaline metals","halogens","noble gases"]

for group in periodicTable:
    for chGroup in chosenGroups:
        if group == chGroup:
            for element in periodicTable[group]:
                chosenElements.append(element)

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


    


#print(periodicTable["alkaline metals"])
#printPeriodic()