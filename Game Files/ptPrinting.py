fullPrintPT = ["[!-]                                                                [!-]",
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

printPT = ["                                                                        ",
           "                                                                        ",
           "                                                                        ",
           "                                                                        ",
           "                                                                        ",
           "                                                                        ",
           "                                                                        ",
           "                                                                        ",
           "                                                                        ",
           "                                                                        "]
def printEmptyPeriodic():
    for row in fullPrintPT:
        print(row)

def printPeriodic(answers, abbreviation, atomicNumber):
    ###This is testing the symbol replacement
    row = 0
    element = atomicNumber

    if element<3:
        element -= 1
        if element==1:
            element +=16
           
    elif element<11:
        row += 1
        element -= 3
        if element>1:
            element +=10
        
    elif element<19:
        row += 2
        element -= 11
        if element>1:
            element +=10

    elif element<37:
        row += 3
        element -= 19

    elif element<55:
        row += 4
        element -= 37

    elif element<57:
        row += 5
        element -= 55

    elif element<72:
        row += 8
        element -= 55

    elif element<87:
        row += 5
        element -= 69

    elif element<89:
        row += 6
        element -= 87

    elif element<104:
        row += 9
        element -= 87

    elif element<112:
        row += 6
        element -= 101

    element *= 4
    if(answers == False):
        printPT[row] = printPT[row][0:element+1] + "X-" + printPT[row][element+3:len(printPT[0])]
    else:
        printPT[row] = printPT[row][0:element+1] + abbreviation + printPT[row][element+3:len(printPT[0])]

    for row in printPT:
        print(row)

