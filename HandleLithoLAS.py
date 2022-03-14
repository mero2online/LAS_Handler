import lasio
import datetime

from GetFunc import *
from HelperFunc import resource_path
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
