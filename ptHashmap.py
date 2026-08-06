### This is setting up the hashmap
periodicTable = {
    "alkaline metals":{
        3  : {"name":"lithium", "atomicNumber":3, "symbol":["█       ","█     █ ","█       ","█    ███","█     █ ","█████ ███"]},
        11 : {"name":"sodium", "atomicNumber":11, "symbol":["█   █     ","██  █     ","█ █ █  ███","█  ██ █   █","█   █ █████","█   █ █   █"]},
        19 : {"name":"potassium", "atomicNumber":19, "symbol":[" █   █"," █  █ "," ███  "," █  █ "," █  █ "," █   █"]},
        37 : {"name":"rubidium", "atomicNumber":37, "symbol":[" ███   █    "," █  █  █    "," ███   ███  "," █ █   █  █ "," █  █  █  █ "," █   █ ███  "]},
        55 : {"name":"caesium", "atomicNumber":55, "symbol":["  ███         "," █   █  ███   "," █      █     "," █      ███   "," █   █     █  ","  ███   ███   "]},
        87 : {"name":"francium", "atomicNumber":87, "symbol":[" █████      "," █          "," ███   ███  "," █     █    "," █     █    "," █     █    "]}
    },
    "alkaline earth metals":{
        4  : {"name":"beryllium", "atomicNumber":4, "symbol":[" ███        "," █  █       "," ███   ███  "," █  █ █████ "," █  █ █     "," ███  ███   "]},
        12 : {"name":"magnesium", "atomicNumber":12, "symbol":[" █   █       "," ██ ██  ███  "," █ █ █ █   █      "," █   █  ███"," █   █     █  "," █   █   ██"]},
        20 : {"name":"calcium", "atomicNumber":20, "symbol":["  ███        "," █   █       "," █      ███  "," █     █   █ "," █   █ █████ ","  ███  █   █ "]},
        38 : {"name":"strontium", "atomicNumber":38, "symbol":["  ███       "," █          ","  ███   ███ ","     █  █   ","     █  █   "," ███    █   "]},
        56 : {"name":"barium", "atomicNumber":56, "symbol":[" ███        "," █  █       "," ███   ███  "," █  █ █   █ "," █  █ █████ "," ███  █   █ "]},
        88 : {"name":"radium", "atomicNumber":88, "symbol":[" ███        "," █  █       "," ███   ███  "," █ █  █   █ "," █  █ █████ "," █   ██   █ "]}
    },
    "post transition metals":{
        13 : {"name":"aluminum", "atomicNumber":13, "symbol":["  ██     ██   "," █  █     █   "," █  █     █   "," ████     █   "," █  █     █   "," █  █    ███  "]},
        31 : {"name":"gallium", "atomicNumber":31, "symbol":["  ███        "," █   █       "," █      ███  "," █  ██ █   █ "," █   █ █████ ","  ███  █   █ "]},
        49 : {"name":"indium", "atomicNumber":49, "symbol":[" ███        ","  █          ","  █     ███  ","  █    █   █ ","  █    █   █ "," ███   █   █ "]},
        50 : {"name":"tin", "atomicNumber":50, "symbol":[" █████    ██   ","   █        █   ","   █        █   ","   █        █   ","   █        █   ","   █       ███  "]},
        81 : {"name":"thallium", "atomicNumber":81, "symbol":["  ███        "," █           ","  ███   ███  ","     █  █   █","     █  █   █"," ███    █   █ "]},
        82 : {"name":"lead", "atomicNumber":82, "symbol":[" ███   █     "," █  █  █     "," ███   ███    "," █     █  █   "," █     █  █   "," █     ███    "]},
        83 : {"name":"bismuth", "atomicNumber":83, "symbol":[" ███     █    "," █  █         "," ███    ███   "," █  █    █    "," █  █    █    "," ███    ███   "]},
        84 : {"name":"polonium", "atomicNumber":84, "symbol":[" ███        "," █  █       "," ███   ███  "," █    █   █ "," █    █   █ "," █     ███  "]}
    },
    "metalloids":{
        5  : {"name":"boron", "atomicNumber":5, "symbol":[" ███   "," █  █  "," ███   "," █  █  "," █  █  "," ███   "]},
        14 : {"name":"silicon", "atomicNumber":14, "symbol":["  ███    █    "," █            ","  ███   ███   ","     █   █    ","     █   █    "," ███    ███   "]},
        32 : {"name":"germanium", "atomicNumber":32, "symbol":["  ███        "," █   █       "," █      ███  "," █  ██ █████ "," █   █ █     ","  ███  ███   "]},
        33 : {"name":"arsenic", "atomicNumber":33, "symbol":["  ██         "," █  █   ███  "," █  █  █     "," ████   ███  "," █  █     █  "," █  █  ███   "]},
        51 : {"name":"antimony", "atomicNumber":51, "symbol":["  ███   █     "," █      █     ","  ███   ███    ","     █  █  █   ","     █  █  █   ","  ███   ███    "]},
        52 : {"name":"tellerium", "atomicNumber":52, "symbol":[" █████       ","   █         ","   █    ███  ","   █   █████ ","   █   █     ","   █    ███  "]}
    },
    "nonmetals":{
        6  : {"name":"carbon", "atomicNumber":6, "symbol":["  ███  "," █   █ "," █     "," █     "," █   █ ","  ███  "]},
        7  : {"name":"nitrogen", "atomicNumber":7, "symbol":[" █   █"," ██  █"," █ █ █"," █  ██"," █   █"," █   █"]},
        8  : {"name":"oxygen", "atomicNumber":8, "symbol":["  ███  "," █   █ "," █   █ "," █   █ "," █   █ ","  ███  "]},
        15 : {"name":"phosphorus", "atomicNumber":15, "symbol":[" ███   "," █  █  "," ███   "," █     "," █     "," █     "]},
        16 : {"name":"sulfur", "atomicNumber":16, "symbol":["  ███  "," █     ","  ███  ","     █ ","     █ "," ███   "]},
        34 : {"name":"selenium", "atomicNumber":34, "symbol":["  ███        "," █           ","  ███   ███  ","     █  ████ ","     █  █    "," ███    ███  "]}
    },
    "halogens":{
        9  : {"name":"fluorine", "atomicNumber":9, "symbol":[" █████"," █     "," ███   "," █     "," █     "," █     "]},
        17 : {"name":"chlorine", "atomicNumber":17, "symbol":["  ███    ██   "," █   █    █   "," █        █   "," █        █   "," █   █    █   ","  ███    ███  "]},
        35 : {"name":"bromine", "atomicNumber":35, "symbol":[" ███        "," █  █       "," ███   ███  "," █  █  █    "," █  █  █    "," ███   █    "]},
        53 : {"name":"iodine", "atomicNumber":53, "symbol":[" ███  ","  █   ","  █   ","  █   ","  █   "," ███  "]},
        85 : {"name":"astatine", "atomicNumber":85, "symbol":["  ██     █    "," █  █    █    "," █  █   ████  "," ████    █    "," █  █    █    "," █  █    █    "]}
    },
    "noble gases":{
        2  : {"name":"helium", "atomicNumber":2, "symbol":[" █   █      "," █   █      "," █████  ███ "," █   █ █████"," █   █ █    "," █   █  ███ "]},
        10 : {"name":"neon", "atomicNumber":10, "symbol":[" █   █      "," ██  █      "," █ █ █  ███ "," █  ██ █████"," █   █ █    "," █   █  ███ "]},
        18 : {"name":"argon", "atomicNumber":18, "symbol":["  ██         "," █  █        "," █  █   ███  "," ████  █     "," █  █  █     "," █  █  █     "]},
        36 : {"name":"krypton", "atomicNumber":36, "symbol":[" █   █      "," █  █       "," ███   ███  "," █  █  █    "," █  █  █    "," █   █ █    "]},
        54 : {"name":"xenon", "atomicNumber":54, "symbol":[" █   █      ","  █ █       ","   █    ███ ","  █ █  █████"," █   █ █    "," █   █  ███ "]},
        86 : {"name":"radon", "atomicNumber":86, "symbol":[" ███        "," █  █       "," ███   ███  "," █ █  █   █ "," █  █ █   █ "," █   ██   █ "]}
    }
}
