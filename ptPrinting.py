printPT = ["[!-]                                                                [!-]",
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

def printPeriodic(answers, atomicNumber):
    ###This is testing the symbol replacement

    element = atomicNumber
    print(element)

    if element<3:
        element -= 1
        if element==1:
            element +=16
        element *= 4
        printPT[0] = printPT[0][0:element+1] + "HI" + printPT[0][element+3:len(printPT[0])]   
    elif element<11:
        element -= 3
        if element>1:
            element +=10
        element *= 4
        printPT[1] = printPT[1][0:element+1] + "HI" + printPT[1][element+3:len(printPT[0])]   
    elif element<19:
        element -= 11
        if element>1:
            element +=10
        element *= 4
        printPT[2] = printPT[2][0:element+1] + "HI" + printPT[2][element+3:len(printPT[0])]   
    elif element<37:
        element -= 19
        element *= 4
        printPT[3] = printPT[3][0:element+1] + "HI" + printPT[3][element+3:len(printPT[0])]
    elif element<55:
        element -= 37
        element *= 4
        printPT[4] = printPT[4][0:element+1] + "HI" + printPT[4][element+3:len(printPT[0])]
    elif element<57:
        element -= 55
        element *= 4
        printPT[5] = printPT[5][0:element+1] + "HI" + printPT[5][element+3:len(printPT[0])]
    elif element<72:
        element -= 55
        element *= 4
        printPT[8] = printPT[8][0:element+1] + "HI" + printPT[8][element+3:len(printPT[0])]
    elif element<87:
        element -= 69
        element *= 4
        printPT[5] = printPT[5][0:element+1] + "HI" + printPT[5][element+3:len(printPT[0])]
    elif element<89:
        element -= 87
        element *= 4
        printPT[6] = printPT[6][0:element+1] + "HI" + printPT[6][element+3:len(printPT[0])]
    elif element<104:
        element -= 87
        element *= 4
        printPT[9] = printPT[9][0:element+1] + "HI" + printPT[9][element+3:len(printPT[0])]
    elif element<112:
        element -= 101
        element *= 4
        printPT[6] = printPT[6][0:element+1] + "HI" + printPT[6][element+3:len(printPT[0])]


    for i in printPT:
        print(i)