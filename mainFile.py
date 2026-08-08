from selectElement import chooseElements, askQuestions

## Greeting
print("\n***Welcome!*** \nType which groups you'd like from the following: \n")
print("Alkaline metals, Alkaline earth metals, Post transition metals")
print("Metalloids, Nonmetals, Halogens, Noble Gases")
#print("Transition Metals, Lathanides, Actinides\n") --> Haven't added it yet!

userGroups = input("Please use commas to separate groups (i.e. halogens, noble gases): ")

## Neat trick I forgot about: You perform changes to an item in a list as you are creating the list
chosenGroups = [group.replace(" ","") for group in userGroups.lower().split(",")]##End of first phase!
## Then, we can send this answer list to selectElement.py!

chooseElements(chosenGroups)
askQuestions()
