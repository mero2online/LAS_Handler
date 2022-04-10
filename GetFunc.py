def GET_LITHO_DATA(litho, lithoValue):
    arr = list(litho)
    for x in range(len(arr)):
        if arr[x] == lithoValue:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_LITHO_EMPTY(litho):
    arr = list(litho)
    for x in range(len(arr)):
        arr[x] = 0
    return arr


def convertNULL(litho):
    arr = list(litho)
    for x in range(len(arr)):
        if arr[x] == -999.2500:
            arr[x] = 0
        else:
            arr[x] = arr[x]
    return arr


def Get_DSG_Formula(r_idx):
    return [f"='original values'!A{r_idx}",
            f"='original values'!B{r_idx}",
            f"='original values'!C{r_idx}+C{r_idx}",
            f"='original values'!D{r_idx}+D{r_idx}",
            f"='original values'!E{r_idx}+E{r_idx}",
            f"='original values'!F{r_idx}+F{r_idx}",
            f"='original values'!G{r_idx}+G{r_idx}",
            f"='original values'!H{r_idx}+H{r_idx}",
            f"='original values'!I{r_idx}+I{r_idx}",
            f"='original values'!J{r_idx}+J{r_idx}",
            f"='original values'!K{r_idx}+K{r_idx}",
            f"='original values'!L{r_idx}+L{r_idx}",
            f"='original values'!M{r_idx}+M{r_idx}",
            f"='original values'!N{r_idx}+N{r_idx}",
            f"='original values'!O{r_idx}+O{r_idx}",
            f"='original values'!P{r_idx}+P{r_idx}",
            f"='original values'!Q{r_idx}+Q{r_idx}",
            f"='original values'!R{r_idx}+R{r_idx}",
            f"='original values'!S{r_idx}+S{r_idx}",
            f"='original values'!T{r_idx}+T{r_idx}",
            f"='original values'!U{r_idx}+U{r_idx}",
            f"='original values'!V{r_idx}+V{r_idx}",
            f"='original values'!W{r_idx}+W{r_idx}",
            f"='original values'!X{r_idx}+X{r_idx}"]


def aggregate_DEPTH_FiveFeet(arr):
    alterArr = []
    chunks = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    for x in chunks:
        if len(x) == 5:
            alterArr.append(x[4])

    return alterArr


def aggregate_ROP_FiveFeet(arr):
    alterArr = []

    for x in range(len(arr)):
        if arr[x] > 0:
            arr[x] = 60/arr[x]
        else:
            arr[x] = 0

    chunks = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    for x in chunks:
        if len(x) == 5:
            alterArr.append(round(sum(x)))

    return alterArr


def getNewPerWellDSG(result):
    PROV, LONG, LATI, XCOORD, YCOORD, ELEV, TD, UWI, WELL, COMP, FLD, LOC, SRVC, DATE = result
    return[
        {
            "mnemonic": "UWI",
            "value": UWI,
            "descr": "UWI",
            "unit": "",
        },
        {
            "mnemonic": "API",
            "value": "XXXXXXXX",
            "descr": "UWI",
            "unit": "",
        },
        {
            "mnemonic": "WELL",
            "value": WELL,
            "descr": "COMMON WELL NAME",
            "unit": "",
        },
        {
            "mnemonic": "COMP",
            "value": COMP,
            "descr": "WELL OPERATOR",
            "unit": "",
        },
        {
            "mnemonic": "FLD",
            "value": FLD,
            "descr": "FIELD",
            "unit": "",
        },
        {
            "mnemonic": "LIC",
            "value": "UNKNOWN",
            "descr": "AUTHORIZATION NO",
            "unit": "",
        },
        {
            "mnemonic": "LOC",
            "value": LOC,
            "descr": "BASIN",
            "unit": "",
        },
        {
            "mnemonic": "CTRY",
            "value": "Saudi Arabia",
            "descr": "COUNTRY",
            "unit": "",
        },
        {
            "mnemonic": "STAT",
            "value": "UNKNOWN",
            "descr": "STATE",
            "unit": "",
        },
        {
            "mnemonic": "CNTY",
            "value": "UNKNOWN",
            "descr": "COUNTY",
            "unit": "",
        },
        {
            "mnemonic": "PROV",
            "value": PROV,
            "descr": "STATE",
            "unit": "",
        },
        {
            "mnemonic": "SRVC",
            "value": SRVC,
            "descr": "COMPANY",
            "unit": "",
        },
        {
            "mnemonic": "DATE",
            "value": DATE,
            "descr": "LOG RUN DATE",
            "unit": "",
        },
        {
            "mnemonic": "LONG",
            "value": LONG,
            "descr": "LONGITUDE",
            "unit": "",
        },
        {
            "mnemonic": "LATI",
            "value": LATI,
            "descr": "LATITUDE",
            "unit": "",
        },
        {
            "mnemonic": "XCOORD",
            "value": XCOORD,
            "descr": "X COORDINATE",
            "unit": "",
        },
        {
            "mnemonic": "YCOORD",
            "value": YCOORD,
            "descr": "Y COORDINATE",
            "unit": "",
        },
        {
            "mnemonic": "ELEV",
            "value": ELEV,
            "descr": "ELEVATION",
            "unit": "FT",
        },
        {
            "mnemonic": "TD",
            "value": TD,
            "descr": "TOTAL DEPTH",
            "unit": "FT",
        },
    ]


def GetDSG_LAS_Header(well, curves):
    return f'~Version Information\n VERS.                  2.0:   CWLS log ASCII Standard -VERSION 2.0\n WRAP.                   NO:   One line per depth step\n\n~Well Information Block\n#MNEM.UNIT     VALUE/NAME     DESCRIPTION\n#---------     -----------    ---------------------------\n{well}\n~Parameter Information Block\n#MNEM.UNIT       Value        Description\n#---------     -----------    ---------------------------\n\nTAPE_NAME. UNK. Las:\nTool_SREING.              UNKNOWN:\nWN   .        UNK: FIELD NAME\nPROJECT.                  :\nSET   .   MUDLOG_LITHOLOGY: \n\n~Curve Information Block\n#MNEM.UNIT                 API CODE     Curve Description\n#---------               -----------    ---------------------------\n{curves}\n'
