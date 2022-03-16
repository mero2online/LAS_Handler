import lasio
import numpy as np
import openpyxl

from HelperFunc import resource_path
from NewCurvesData import newPerCurves, newPerLithCurves, modPerCurves
from GetFunc import convertNULL, GET_LITHO_EMPTY


def gen_litho_Percent_LAS(filename):
    las = lasio.read(filename)

    for idx, x in enumerate(las.keys()):
        if (idx == 21 or idx == 29 or idx == 30 or idx == 31 or idx == 32 or idx == 33):
            las.delete_curve(x)

    for idx, x in enumerate(las.keys()):
        res = convertNULL(las[x])
        las.delete_curve(x)
        las.append_curve(newPerCurves[idx], res, descr=newPerCurves[idx])

    las.write(resource_path('draft.las'), fmt='%.0f', len_numeric_field=5)
    las.to_excel(resource_path('draft.xlsx'))
    workbook = openpyxl.load_workbook(resource_path('draft.xlsx'))
    std = workbook.get_sheet_by_name('Header')
    workbook.remove_sheet(std)
    workbook.save(resource_path('draft.xlsx'))

    DSG()
    LITHOLOGY()

#
# DSG
#


def DSG():
    las = lasio.read(resource_path('draft.las'))
    for idx, x in enumerate(las.keys()):
        if (idx == 18):
            data = [0]*len(las[x])
            las.delete_curve(x)
            las.insert_curve(17, x, data)

    for idx, x in enumerate(las.keys()):
        if (idx == 9 or idx == 10 or idx == 16 or idx == 25):
            las.delete_curve(x)

    las.write(resource_path('draft_DSG.las'), fmt='%.0f', len_numeric_field=5)
    las.to_excel(resource_path('draft_DSG.xlsx'))
    workbook = openpyxl.load_workbook(resource_path('draft_DSG.xlsx'))
    std = workbook.get_sheet_by_name('Header')
    workbook.remove_sheet(std)
    workbook.save(resource_path('draft_DSG.xlsx'))

    f = open(resource_path('draft_DSG.las'), 'r')
    txt = f.read()
    f.close()

    firstRow = ' '.join(las.keys())
    startThree = '~ASCII -----------------------------------------------------'
    data_DSG = txt[txt.find(startThree)+len(startThree):len(txt)-1]
    finalData = f'{firstRow}{data_DSG}'

    f = open(resource_path('draft_DSG.las'), 'w')
    f.write(finalData)
    f.close()

#
# LITHOLOGY
#


def LITHOLOGY():
    las = lasio.read(resource_path('draft.las'))
    newLas = lasio.LASFile()
    newLas.add_curve('DEPTH', las['DEPTH'], unit='ft')

    for idx, x in enumerate(newPerLithCurves):
        if idx <= 19:
            newLas.add_curve(x, las[modPerCurves[idx]], unit='%')
        else:
            newLas.add_curve(x, GET_LITHO_EMPTY(las['DEPTH']), unit='%')

    newLas.write(resource_path('draft_LITHOLOGY.las'), fmt='%.0f', len_numeric_field=5)
    newLas.to_excel(resource_path('draft_LITHOLOGY.xlsx'))
    workbook = openpyxl.load_workbook(resource_path('draft_LITHOLOGY.xlsx'))
    std = workbook.get_sheet_by_name('Header')
    workbook.remove_sheet(std)
    workbook.save(resource_path('draft_LITHOLOGY.xlsx'))

    f = open(resource_path('draft_LITHOLOGY.las'), 'r')
    txt = f.read()
    f.close()

    firstRow = ' '.join(newLas.keys())
    startThree = '~ASCII -----------------------------------------------------'
    data_LITHOLOGY = txt[txt.find(startThree)+len(startThree):len(txt)-1]
    finalData = f'{firstRow}{data_LITHOLOGY}'

    f = open(resource_path('draft_LITHOLOGY.las'), 'w')
    f.write(finalData)
    f.close()
