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

newDrillCurves = [
    {
        "name": "DEPTH",
        "desc": "Depth",
        "unit": "FT"
    },
    {
        "name": "DEPTH_ORIG",
        "desc": "Depth Original Measured",
        "unit": "FT"
    },
    {
        "name": "BIT_SIZE",
        "desc": "Bit Size",
        "unit": "INS"
    },
    {
        "name": "FLWPMPS",
        "desc": "Flowrate Mud Pumps",
        "unit": "GAL(U.S.)/MIN"
    },
    {
        "name": "FLWOUT",
        "desc": "Mud Flow Out",
        "unit": "GAL(U.S.)/MIN"
    },
    {
        "name": "TEMP_MUD_IN",
        "desc": "Mud Temperature In",
        "unit": "DEGF"
    },
    {
        "name": "TEMP_MUD_OUT",
        "desc": "Mud Temperature Out",
        "unit": "DEGF"
    },
    {
        "name": "RHO_MUD_IN",
        "desc": "Mud Density IN",
        "unit": "LBCF"
    },
    {
        "name": "RHO_MUD_OUT",
        "desc": "Mud Density Out",
        "unit": "LBCF"
    },
    {
        "name": "ROP",
        "desc": "Rate Of Penetration",
        "unit": "FT/HR"
    },
    {
        "name": "RPM",
        "desc": "Revolution Per Minute",
        "unit": "RPM"
    },
    {
        "name": "RPMTI",
        "desc": "TOP DRIVE RPM",
        "unit": "RPM"
    },
    {
        "name": "RPMMI",
        "desc": "MUD MOTOR RPM",
        "unit": "RPM"
    },
    {
        "name": "TORQUE",
        "desc": "Tourqe",
        "unit": "KPOUNDF*FT"
    },
    {
        "name": "WOB",
        "desc": "Weight On Bit",
        "unit": "KLBF"
    },
    {
        "name": "HKLI",
        "desc": "Hookload",
        "unit": "KLBF"
    },
    {
        "name": "SPP",
        "desc": "standpipe pressure",
        "unit": "PSI"
    },
    {
        "name": "COND_MUD_IN",
        "desc": "Conductivity In",
        "unit": "OHMM"
    },
    {
        "name": "COND_MUD_OUT",
        "desc": "Conductivity Out",
        "unit": "OHMM"
    },
    {
        "name": "TOTAL_PIT_VOL",
        "desc": "Total Pit Volume",
        "unit": "BBLS"
    },
    {
        "name": "CO2",
        "desc": "Carbon Dioxide",
        "unit": "PPM"
    },
    {
        "name": "H2S",
        "desc": "Hydrogen Sulphide",
        "unit": "PPM"
    },
    {
        "name": "LAG_TIME",
        "desc": "Lagged Sample Time",
        "unit": "MINS"
    },
]
newGasCurves = [
    {
        "name": "DEPTH",
        "desc": " 1 Hole Depth",
        "unit": "ft"
    },
    {
        "name": "MUDGAS_C1",
        "desc": " 2 Delta Methane",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_C1_IN",
        "desc": " 3 Methane In",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_C1_OUT",
        "desc": " 4 Methane Out",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_C2",
        "desc": " 5 Delta Ethane",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_C2_IN",
        "desc": " 6 Ethane In",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_C2_OUT",
        "desc": " 7 Ethane Out",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_C3",
        "desc": " 8 Delta Propane",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_C3_IN",
        "desc": " 9 Propane In",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_C3_OUT",
        "desc": "10 Propane Out",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_IC4",
        "desc": "11 Delta Iso-Butane",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_IC4_IN",
        "desc": "12 Iso-Butane In",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_IC4_OUT",
        "desc": "13 Iso-Butane Out",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_NC4",
        "desc": "14 Delta N-Butane",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_NC4_IN",
        "desc": "15 N-Butane In",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_NC4_OUT",
        "desc": "16 N-Butane Out",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_IC5",
        "desc": "17 Delta Iso-Pentane",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_IC5_IN",
        "desc": "18 Iso-Pentane In",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_IC5_OUT",
        "desc": "19 Iso-Pentane Out",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_NC5",
        "desc": "20 Delta N-Pentane",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_NC5_IN",
        "desc": "21 N-Pentane In",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_NC5_OUT",
        "desc": "22 N-Pentane Out",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_HYDC",
        "desc": "23 Hydrocarbons",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_HYDC_IN",
        "desc": "24 Hydrocarbons In",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_HYDC_OUT",
        "desc": "25 Hydrocarbons Out",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_TGAS_HOT",
        "desc": "26 Hydrocarbons",
        "unit": "ppm"
    },
    {
        "name": "MUDGAS_CO2",
        "desc": "27 Carbon dioxide OUT",
        "unit": "ppm"
    },
]
