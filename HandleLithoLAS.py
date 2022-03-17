import lasio
import datetime
from openpyxl import Workbook

from my_const import *
from GetFunc import *
from HelperFunc import resource_path, readLocalFile, writeLocalFile
from NewCurvesData import newLithoCurves


def gen_litho_LAS(filename):
    las = lasio.read(filename)

    # print(las.keys())
    # LTY_remove_NaN = np.nan_to_num(LTY, copy=True)
    # volcut_anhy = [math.trunc(value) for value in LTY_remove_NaN]
    # print(las.get_curve('LTY'))
    # print(las['LTY'])

    wellNameOriginal = las.well.WELL.value
    finalWellName = wellNameOriginal[wellNameOriginal.find(
        '(')+len('('):wellNameOriginal.rfind(')')]
    las.well.WELL = finalWellName

    day = datetime.datetime.now().strftime("%d")
    month = datetime.datetime.now().strftime("%b").upper()
    year = datetime.datetime.now().strftime("%Y")
    finalWellDate = f'{day}_{month}_{year}'
    las.well.DATE = finalWellDate

    las.well.SRVC = 'EXLOG'

    LTY = las['LTY']

    las.append_curve('DEPTH', las['DMEA'],
                     unit='ft', descr='1 Hole Depth')

    for idx in range(len(newLithoCurves)):
        VOLCUT = GET_LITHO_EMPTY(LTY) if newLithoCurves[idx]['value'] == 0 else GET_LITHO_DATA(
            LTY, newLithoCurves[idx]['value'])
        las.append_curve(newLithoCurves[idx]['name'], VOLCUT,
                         unit='%', descr=newLithoCurves[idx]['desc'])

    las.delete_curve('LTY')
    las.delete_curve('DMEA')

    las.write(resource_path('draft.las'), fmt='%.0f', len_numeric_field=5)

    txt = readLocalFile(resource_path('draft.las'))

    startOne = '~Well ------------------------------------------------------'
    endOne = '~Curve Information -----------------------------------------'
    textOneLas = txt[txt.find(startOne)+len(startOne):txt.rfind(endOne)]

    startTwo = '~Curve Information -----------------------------------------'
    endTwo = '~Params ----------------------------------------------------'
    textTwoLas = txt[txt.find(startTwo)+len(startTwo):txt.rfind(endTwo)]

    startThree = '~ASCII -----------------------------------------------------'
    textThreeLas = txt[txt.find(startThree)+len(startThree):len(txt)-1]

    finalData = f'{text1}{textOneLas}{text2}{textTwoLas}{text3}{textThreeLas}'

    writeLocalFile(resource_path('draft.las'), finalData)

    finalFileName = f'{las.well.WELL.value}_INTERPRETIVE_LITHOLOGY_{las.well.DATE.value}'
    writeLocalFile(resource_path(f'out\\{finalFileName}.las'), finalData)

    wb = Workbook()
    ws1 = wb.active
    data = finalData.splitlines()
    for idx, row in enumerate(data):
        if idx <= 51:
            ws1.append([row])
        elif idx == 52:
            one = row.split()
            two = one[2:len(one)]
            two.insert(0, ' '.join([one[0], one[1]]))
            ws1.append(two)
        else:
            ws1.append([int(x) for x in row.split()])
    
    wb.save(resource_path(f'out\\{finalFileName}.xlsx'))
