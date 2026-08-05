'''
    Idea: Memorization game for Periodic Table

    * Start: 
    * Present an Element block
    * Ask user to fill out details
    * Update Periodic Table
    * If correct, insert the letter where it belongs
    * If not, then use an X instead
    
    To figure out:
    * Ask which group(s) to use
    * Continously update the Periodic Table correctly a.k.a
      have the symbol match the slot

    Ideas:
    * Since every element has an Atomic Number, we can just
      use that to figure out which row and column to write
      it into. 
      Only issue is knowing how to replace the slot

      I.E.
      [!-]        [!-]
      to 
      [!-]        [He]

      Mmhh, you have to split the string, right?
      Then insert the updated block where it should be, right?
      Plus, all blocks have the same width so we know when to cut

    Also, how to access the answers for each element?
    And how do we choose from the available groups?

    I'm thinking we have a separate list with all possible elements to choose from.
    We can fill that list by going through each group selected and inserting all
    atomic numbers they have.
    Then, we can have a loop going through them randomly, randomly choosing an element
    to ask about and then popping their atomic number from the selection list.
    Finally, we check if the list is empty yet, and if not then we keep going until it's done.  
'''
#Let's start setting up an example hashmap for the Alkaline Metals

periodicTable = {
    "alkaline  metals":{
        3  : {"name":"lithium", "atomicNumber":3, "symbol":["█       ","█     █ ","█       ","█    ███","█     █ ","█████ ███"]},
        11 : {"name":"sodium", "atomicNumber":11, "symbol":["█   █     ","██  █     ","█ █ █  ███","█  ██ █   █","█   █ █████","█   █ █   █"]},
        19 : {"name":"potassium", "atomicNumber":19, "symbol":[" █   █"," █  █ "," ███  "," █  █ "," █  █ "," █   █"]},
        37 : {"name":"rubidium", "atomicNumber":37, "symbol":[" ███   █    "," █  █  █    "," ███   ███  "," █ █   █  █ "," █  █  █  █ "," █   █ ███  "]},
        55 : {"name":"caesium", "atomicNumber":55, "symbol":["  ███         "," █   █  ███   "," █      █     "," █      ███   "," █   █     █  ","  ███   ███   "]},
        87 : {"name":"francium", "atomicNumber":87, "symbol":[" █████      "," █          "," ███   ███  "," █     █    "," █     █    "," █     █    "]}
    }
}

#now let me test smth
for j in periodicTable["alkaline  metals"]:
    for i in periodicTable["alkaline  metals"][j]["symbol"]:
        print(i)
