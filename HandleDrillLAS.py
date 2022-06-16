import lasio

from my_const import *
from GetFunc import *
from HelperFunc import getFinalWellDate, resource_path, readLocalFile, writeLocalFile
from NewCurvesData import newDrillCurves


def gen_DRILL_LAS(filename):
    las = lasio.read(filename)

    wellNameOriginal = las.well.WELL.value
    finalWellName = wellNameOriginal[wellNameOriginal.find(
        '(')+len('('):wellNameOriginal.rfind(')')]
    las.well.WELL = finalWellName

    finalWellDate = getFinalWellDate()
    las.well.DATE = finalWellDate

    las.well.SRVC = 'EXLOG'

    for idx, x in enumerate(las.keys()):
        mnemonic = newDrillCurves[idx]['name']
        data = las[x] if idx <= 1 else las[x]+las[las.keys()[idx-1]]
        unit = newDrillCurves[idx]['unit']
        descr = newDrillCurves[idx]['desc']
        las.delete_curve(x)
        las.insert_curve(idx, mnemonic, data, unit=unit, descr=descr)

    las.write(resource_path('draft.las'), fmt='%.4f', len_numeric_field=5)

    txt = readLocalFile(resource_path('draft.las'))
    textOriginal = readLocalFile(resource_path('input.las'))
    startOne = '~Well ------------------------------------------------------'
    endOne = '~Curve Information -----------------------------------------'
    textOneLas = txt[txt.find(startOne)+len(startOne):txt.rfind(endOne)]

    startTwo = '~Curve Information -----------------------------------------'
    endTwo = '~Params ----------------------------------------------------'
    textTwoLas = txt[txt.find(startTwo)+len(startTwo):txt.rfind(endTwo)]

    startThree = 'WOBI        HKLI        SPPI        MCIA        MCOA        TVT1        CO2_1       AH2S1       UD1         '
    textThreeLas = textOriginal[textOriginal.find(startThree)+len(startThree):len(textOriginal)-1]

    finalData = f'{text1}{textOneLas}{text8}{textTwoLas}{text9}{textThreeLas}'

    writeLocalFile(resource_path('draft.las'), finalData)

    finalFileNameLas = f'{las.well.WELL.value}_DRILLING_{las.well.DATE.value}'
    writeLocalFile(resource_path(f'out\\{finalFileNameLas}.las'), finalData)
