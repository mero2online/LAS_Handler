newPerCurves = ['DEPTH', 'HAL', 'ANHY', 'GYP', 'DOL', 'CALDOL', 'ARGDOL', 'SNDDOL', 'CCCARB',
                'CAL', 'CALLS', 'DOLLS', 'LS', 'ARGLS', 'SNDLS', 'MARL', 'CLAY', 'SH', 'SNDSH',
                'SST', 'SAND', 'CONG', 'CHERT', 'COAL', 'IGN', 'MET', 'UNK', 'CEMENT']

modPerCurves = ['ANHY', 'ARGDOL', 'ARGLS', 'CALDOL', 'CALLS', 'CEMENT', 'CHERT', 'CLAY', 'COAL',
                'CONG', 'DOL', 'DOLLS', 'GYP', 'HAL', 'IGN', 'LS', 'MARL', 'SAND', 'SH', 'SST']

newPerLithCurves = [
    {
        "name": "VOLCUT_ANHY",
        "desc": "2 Anhydrite",
    },
    {
        "name": "VOLCUT_ARGDOL",
        "desc": "3 Argillaceous Dolomite",
    },
    {
        "name": "VOLCUT_ARGLS",
        "desc": "4 Argillaceous Limestone",
    },
    {
        "name": "VOLCUT_CALDOL",
        "desc": "5 Calcarenite Dolomite",
    },
    {
        "name": "VOLCUT_CALLS",
        "desc": "6 Calcarenite Limestone",
    },
    {
        "name": "VOLCUT_CEMENT",
        "desc": "7 Cement",
    },
    {
        "name": "VOLCUT_CHERT",
        "desc": "8 Chert",
    },
    {
        "name": "VOLCUT_CLAY",
        "desc": "9 Clay",
    },
    {
        "name": "VOLCUT_COAL",
        "desc": "10 Coal_Lignite_TAR",
    },
    {
        "name": "VOLCUT_CONG",
        "desc": "11 Conglomerate",
    },
    {
        "name": "VOLCUT_DOL",
        "desc": "12 Dolomite",
    },
    {
        "name": "VOLCUT_DOLLS",
        "desc": "13 Dolomitic Limestone",
    },
    {
        "name": "VOLCUT_GYP",
        "desc": "14 Gypsum",
    },
    {
        "name": "VOLCUT_HAL",
        "desc": "15 Halite",
    },
    {
        "name": "VOLCUT_IGN",
        "desc": "16 Igneous",
    },
    {
        "name": "VOLCUT_LS",
        "desc": "17 Limestone",
    },
    {
        "name": "VOLCUT_MARL",
        "desc": "18 Marl",
    },
    {
        "name": "VOLCUT_SAND",
        "desc": "19 Sandstone",
    },
    {
        "name": "VOLCUT_SH",
        "desc": "20 Shale",
    },
    {
        "name": "VOLCUT_SST",
        "desc": "21 Siltstone",
    },
    {
        "name": "CALC_M",
        "desc": "22 Calcimetry Limestone",
    },
    {
        "name": "DOLO_M",
        "desc": "23 Calcimetry Dolomite",
    },
    {
        "name": "DIR_FLUO",
        "desc": "24 Direct Fluorescence",
    },
    {
        "name": "CUT_FLUO",
        "desc": "25 Fluorescent Cut",
    },
]

newLithoCurves = [
    {
        "name": "VOLCUT_ANHY",
        "desc": "2 Anhydrite",
        "value": 2
    },
    {
        "name": "VOLCUT_ARGDOL",
        "desc": "3 Argillaceous Dolomite",
        "value": 6
    },
    {
        "name": "VOLCUT_ARGLS",
        "desc": "4 Argillaceous Limestone",
        "value": 13
    },
    {
        "name": "VOLCUT_CALDOL",
        "desc": "5 Calcarenite Dolomite",
        "value": 5
    },
    {
        "name": "VOLCUT_CALLS",
        "desc": "6 Calcarenite Limestone",
        "value": 10
    },
    {
        "name": "VOLCUT_CEMENT",
        "desc": "7 Cement",
        "value": 28
    },
    {
        "name": "VOLCUT_CHERT",
        "desc": "8 Chert",
        "value": 23
    },
    {
        "name": "VOLCUT_CLAY",
        "desc": "9 Clay",
        "value": 16
    },
    {
        "name": "VOLCUT_COAL",
        "desc": "10 Coal_Lignite_TAR",
        "value": 24
    },
    {
        "name": "VOLCUT_CONG",
        "desc": "11 Conglomerate",
        "value": 22
    },
    {
        "name": "VOLCUT_DOL",
        "desc": "12 Dolomite",
        "value": 4
    },
    {
        "name": "VOLCUT_DOLLS",
        "desc": "13 Dolomitic Limestone",
        "value": 11
    },
    {
        "name": "VOLCUT_GYP",
        "desc": "14 Gypsum",
        "value": 3
    },
    {
        "name": "VOLCUT_HAL",
        "desc": "15 Halite",
        "value": 1
    },
    {
        "name": "VOLCUT_IGN",
        "desc": "16 Igneous",
        "value": 25
    },
    {
        "name": "VOLCUT_LS",
        "desc": "17 Limestone",
        "value": 12
    },
    {
        "name": "VOLCUT_MARL",
        "desc": "18 Marl",
        "value": 15
    },
    {
        "name": "VOLCUT_SAND",
        "desc": "19 Sandstone",
        "value": 20
    },
    {
        "name": "VOLCUT_SH",
        "desc": "20 Shale",
        "value": 17
    },
    {
        "name": "VOLCUT_SST",
        "desc": "21 Siltstone",
        "value": 19
    },
]

newPerCurvesDSG = [
    {
        "name": "DEPTH",
        "desc": "Hole Depth",
    },
    {
        "name": "HALITE",
        "desc": "1 halite",
    },
    {
        "name": "ANHY",
        "desc": "2 Anhydrite",
    },
    {
        "name": "GYPSUM",
        "desc": "3 GYPSUM",
    },
    {
        "name": "DOLO",
        "desc": "4 dolomite",
    },
    {
        "name": "CALCDOLO",
        "desc": "5 calcarenite Dolomite",
    },
    {
        "name": "ARGDOLO",
        "desc": "6 Argillaceous Dolomite",
    },
    {
        "name": "SNDDOLO",
        "desc": "7 Sandy Dolomite",
    },
    {
        "name": "CARBON",
        "desc": "8 Carbonate ",
    },
    {
        "name": "DOLOLIME",
        "desc": "9 Dolomitic Limestone",
    },
    {
        "name": "LIME",
        "desc": "10 Limestone",
    },
    {
        "name": "ARGLIME",
        "desc": "11 Argillaceous Limestone ",
    },
    {
        "name": "SANDLIME",
        "desc": "12 Sandy Limestone",
    },
    {
        "name": "MARL",
        "desc": "16 Marl",
    },
    {
        "name": "SHALE",
        "desc": "17 Shale",
    },
    {
        "name": "SILTSHALE",
        "desc": "18 Silty Shale",
    },
    {
        "name": "SILT",
        "desc": "19 Siltstone",
    },
    {
        "name": "SANDSTONE",
        "desc": "20 Sandstone",
    },
    {
        "name": "CONGLOM",
        "desc": "21 Conglomerate",
    },
    {
        "name": "CHERT",
        "desc": "22 Chert",
    },
    {
        "name": "COAL",
        "desc": "23 Coal",
    },
    {
        "name": "IGNEOUS",
        "desc": "24 Igneous",
    },
    {
        "name": "CEMENT",
        "desc": "25 Cement",
    },
    {
        "name": "UNKNOWN",
        "desc": "26 Unknown",
    },
]
