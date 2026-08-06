#Let's start setting up an example hashmap for the Alkaline Metals
import random
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

printPT = ["[!-]                                                            [!-]",
           "[!-][!-]                                        [!-][!-][!-][!-][!-][!-]",
           "[!-][!-]                                        [!-][!-][!-][!-][!-][!-]",
           "[!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-]",
           "[!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-]",
           "[!-][!-]  ^ [!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-]",
           "[!-][!-]  ^ [!-][!-][!-][!-][!-][!-][!-][!-]",
           "          ^",
           "        [!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-]",
           "        [!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-]"
          ]

element = random.randint(1,50)
print(element)
if element<3:
    print(1)
elif element<11:
    print(2)
elif element<19:
    print(3)
elif element<37:
    element -= 19
    element *= 4
    printPT[3] = printPT[3][0:element+1] + "HI" + printPT[3][element+3:len(printPT[3])]
    print(printPT[3])
elif element<55:
    element -= 55
    element *= 4
    printPT[3] = printPT[3][0:element+1] + "HI" + printPT[3][element+3:len(printPT[3])]
    print(printPT[3])