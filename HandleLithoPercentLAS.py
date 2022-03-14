import lasio
import numpy as np
import openpyxl

from HelperFunc import resource_path


def gen_litho_Percent_LAS(filename):
    las = lasio.read(filename)

    newCurves = ['DEPTH', 'HAL', 'ANHY', 'GYP', 'DOL', 'CALDOL', 'ARGDOL', 'SNDDOL', 'CCCARB', 'CAL', 'CALLS', 'DOLLS', 'LS', 'ARGLS',
                 'SNDLS', 'MARL', 'CLAY', 'SH', 'SNDSH', 'SST', 'SAND', 'CONG', 'CHERT', 'COAL', 'IGN', 'MET', 'UNK', 'CEMENT']
    
    for idx, x in enumerate(las.keys()):
        if (idx == 21 or idx == 29 or idx == 30 or idx == 31 or idx == 32 or idx == 33):
            las.delete_curve(x)

    for idx, x in enumerate(las.keys()):
        res = convertNULL(las[x])
        las.delete_curve(x)
        las.append_curve(newCurves[idx], res, descr=newCurves[idx])

    las.write(resource_path('draft.las'), fmt='%.0f', len_numeric_field=5)
    las.to_excel(resource_path('draft.xlsx'))
    workbook = openpyxl.load_workbook(resource_path('draft.xlsx'))
    std = workbook.get_sheet_by_name('Header')
    workbook.remove_sheet(std)
    workbook.save(resource_path('draft.xlsx'))


def convertNULL(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == -999.2500:
            arr[x] = 0
        else:
            arr[x] = arr[x]
    return arr
