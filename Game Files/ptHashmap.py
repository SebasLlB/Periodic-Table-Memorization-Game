''' This is the Periodic Table Hashmap
    Categorized as:
        Periodic Table
        -> Gropus
           -> Atomic Number
              -> Abbr.
              -> Name
              -> Symbol broken into rows
'''
periodicTable = {
    "alkalineMetals":{
        3  : {"abbr":"Li", "name":"lithium", "symbol":["█       ","█     █ ","█       ","█    ███","█     █ ","█████ ███"]},
        11 : {"abbr":"Na", "name":"sodium", "symbol":["█   █     ","██  █     ","█ █ █  ███","█  ██ █   █","█   █ █████","█   █ █   █"]},
        19 : {"abbr":"K ", "name":"potassium", "symbol":[" █   █"," █  █ "," ███  "," █  █ "," █  █ "," █   █"]},
        37 : {"abbr":"Rb", "name":"rubidium", "symbol":[" ███   █    "," █  █  █    "," ███   ███  "," █ █   █  █ "," █  █  █  █ "," █   █ ███  "]},
        55 : {"abbr":"Cs", "name":"caesium", "symbol":["  ███         "," █   █  ███   "," █      █     "," █      ███   "," █   █     █  ","  ███   ███   "]},
        87 : {"abbr":"Fr", "name":"francium", "symbol":[" █████      "," █          "," ███   ███  "," █     █    "," █     █    "," █     █    "]}
    },
    "alkalineEarthMetals":{
        4  : {"abbr":"Be", "name":"beryllium", "symbol":[" ███        "," █  █       "," ███   ███  "," █  █ █████ "," █  █ █     "," ███  ███   "]},
        12 : {"abbr":"Mg", "name":"magnesium", "symbol":[" █   █       "," ██ ██  ███  "," █ █ █ █   █      "," █   █  ███"," █   █     █  "," █   █   ██"]},
        20 : {"abbr":"Ca", "name":"calcium", "symbol":["  ███        "," █   █       "," █      ███  "," █     █   █ "," █   █ █████ ","  ███  █   █ "]},
        38 : {"abbr":"Sr", "name":"strontium", "symbol":["  ███       "," █          ","  ███   ███ ","     █  █   ","     █  █   "," ███    █   "]},
        56 : {"abbr":"Ba", "name":"barium", "symbol":[" ███        "," █  █       "," ███   ███  "," █  █ █   █ "," █  █ █████ "," ███  █   █ "]},
        88 : {"abbr":"Ra", "name":"radium", "symbol":[" ███        "," █  █       "," ███   ███  "," █ █  █   █ "," █  █ █████ "," █   ██   █ "]}
    },
    "postTransitionMetals":{
        13 : {"abbr":"Al", "name":"aluminum", "symbol":["  ██     ██   "," █  █     █   "," █  █     █   "," ████     █   "," █  █     █   "," █  █    ███  "]},
        31 : {"abbr":"Ga", "name":"gallium", "symbol":["  ███        "," █   █       "," █      ███  "," █  ██ █   █ "," █   █ █████ ","  ███  █   █ "]},
        49 : {"abbr":"In", "name":"indium", "symbol":[" ███        ","  █          ","  █     ███  ","  █    █   █ ","  █    █   █ "," ███   █   █ "]},
        50 : {"abbr":"Sb", "name":"tin", "symbol":[" █████    ██   ","   █        █   ","   █        █   ","   █        █   ","   █        █   ","   █       ███  "]},
        81 : {"abbr":"Tl", "name":"thallium", "symbol":["  ███        "," █           ","  ███   ███  ","     █  █   █","     █  █   █"," ███    █   █ "]},
        82 : {"abbr":"Pb", "name":"lead", "symbol":[" ███   █     "," █  █  █     "," ███   ███    "," █     █  █   "," █     █  █   "," █     ███    "]},
        83 : {"abbr":"Bi", "name":"bismuth", "symbol":[" ███     █    "," █  █         "," ███    ███   "," █  █    █    "," █  █    █    "," ███    ███   "]},
        84 : {"abbr":"Po", "name":"polonium", "symbol":[" ███        "," █  █       "," ███   ███  "," █    █   █ "," █    █   █ "," █     ███  "]}
    },
    "metalloids":{
        5  : {"abbr":"Bo", "name":"boron","symbol":[" ███   "," █  █  "," ███   "," █  █  "," █  █  "," ███   "]},
        14 : {"abbr":"Si", "name":"silicon", "symbol":["  ███    █    "," █            ","  ███   ███   ","     █   █    ","     █   █    "," ███    ███   "]},
        32 : {"abbr":"Ge", "name":"germanium", "symbol":["  ███        "," █   █       "," █      ███  "," █  ██ █████ "," █   █ █     ","  ███  ███   "]},
        33 : {"abbr":"As", "name":"arsenic", "symbol":["  ██         "," █  █   ███  "," █  █  █     "," ████   ███  "," █  █     █  "," █  █  ███   "]},
        51 : {"abbr":"Sb", "name":"antimony", "symbol":["  ███   █     "," █      █     ","  ███   ███    ","     █  █  █   ","     █  █  █   ","  ███   ███    "]},
        52 : {"abbr":"Te", "name":"tellerium", "symbol":[" █████       ","   █         ","   █    ███  ","   █   █████ ","   █   █     ","   █    ███  "]}
    },
    "nonmetals":{
        1  : {"abbr":"H ", "name":"hydrogen", "symbol":[" █   █"," █   █"," █████"," █   █"," █   █"," █   █"]},
        6  : {"abbr":"C ", "name":"carbon", "symbol":["  ███  "," █   █ "," █     "," █     "," █   █ ","  ███  "]},
        7  : {"abbr":"N ", "name":"nitrogen", "symbol":[" █   █"," ██  █"," █ █ █"," █  ██"," █   █"," █   █"]},
        8  : {"abbr":"O ", "name":"oxygen", "symbol":["  ███  "," █   █ "," █   █ "," █   █ "," █   █ ","  ███  "]},
        15 : {"abbr":"P ", "name":"phosphorus", "symbol":[" ███   "," █  █  "," ███   "," █     "," █     "," █     "]},
        16 : {"abbr":"S ", "name":"sulfur", "symbol":["  ███  "," █     ","  ███  ","     █ ","     █ "," ███   "]},
        34 : {"abbr":"Se", "name":"selenium", "symbol":["  ███        "," █           ","  ███   ███  ","     █  ████ ","     █  █    "," ███    ███  "]}
    },
    "halogens":{
        9  : {"abbr":"F ", "name":"fluorine", "symbol":[" █████"," █     "," ███   "," █     "," █     "," █     "]},
        17 : {"abbr":"Cl", "name":"chlorine", "symbol":["  ███    ██   "," █   █    █   "," █        █   "," █        █   "," █   █    █   ","  ███    ███  "]},
        35 : {"abbr":"Br", "name":"bromine", "symbol":[" ███        "," █  █       "," ███   ███  "," █  █  █    "," █  █  █    "," ███   █    "]},
        53 : {"abbr":"I ", "name":"iodine", "symbol":[" ███  ","  █   ","  █   ","  █   ","  █   "," ███  "]},
        85 : {"abbr":"At", "name":"astatine", "symbol":["  ██     █    "," █  █    █    "," █  █   ████  "," ████    █    "," █  █    █    "," █  █    █    "]}
    },
    "nobleGases":{
        2  : {"abbr":"He", "name":"helium", "symbol":[" █   █      "," █   █      "," █████  ███ "," █   █ █████"," █   █ █    "," █   █  ███ "]},
        10 : {"abbr":"Ne", "name":"neon", "symbol":[" █   █      "," ██  █      "," █ █ █  ███ "," █  ██ █████"," █   █ █    "," █   █  ███ "]},
        18 : {"abbr":"Ar", "name":"argon", "symbol":["  ██         "," █  █        "," █  █   ███  "," ████  █     "," █  █  █     "," █  █  █     "]},
        36 : {"abbr":"Kr", "name":"krypton", "symbol":[" █   █      "," █  █       "," ███   ███  "," █  █  █    "," █  █  █    "," █   █ █    "]},
        54 : {"abbr":"Xe", "name":"xenon", "symbol":[" █   █      ","  █ █       ","   █    ███ ","  █ █  █████"," █   █ █    "," █   █  ███ "]},
        86 : {"abbr":"Rn", "name":"radon", "symbol":[" ███        "," █  █       "," ███   ███  "," █ █  █   █ "," █  █ █   █ "," █   ██   █ "]}
    }
}
