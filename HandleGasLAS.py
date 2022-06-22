import lasio

from my_const import *
from HelperFunc import getFinalWellDate, resource_path, readLocalFile, writeLocalFile
from NewCurvesData import newGasCurves


def gen_GAS_LAS(filename):
    las = lasio.read(filename)

    wellNameOriginal = las.well.WELL.value
    finalWellName = wellNameOriginal[wellNameOriginal.find(
        '(')+len('('):wellNameOriginal.rfind(')')]
    las.well.WELL = finalWellName

    finalWellDate = getFinalWellDate()
    las.well.DATE = finalWellDate

    las.well.SRVC = 'EXLOG'

    for idx, x in enumerate(las.keys()):
        mnemonic = newGasCurves[idx]['name']
        data = las[x] if idx <= 1 else las[x]+las[las.keys()[idx-1]]
        unit = newGasCurves[idx]['unit']
        descr = newGasCurves[idx]['desc']
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

    startThree = '~A  DMEA        METH        METH2       METH1       ETH         ETH2        ETH1        PRP         PRP2        PRP1        IBUT        IBUT2       IBUT1       NBUT        NBUT2       NBUT1       IPEN        IPEN2       IPEN1       NPEN        NPEN2       NPEN1       GASS1       HYDC4       HYDC5       GASS        CO2_1       '
    textThreeLas = textOriginal[textOriginal.find(startThree)+len(startThree):len(textOriginal)-1]

    finalData = f'{text1}{textOneLas}{text10}{textTwoLas}{text11}{textThreeLas}'

    writeLocalFile(resource_path('draft.las'), finalData)

    finalFileNameLas = f'{las.well.WELL.value}_GAS_{las.well.DATE.value}'
    writeLocalFile(resource_path(f'out\\{finalFileNameLas}.las'), finalData)
