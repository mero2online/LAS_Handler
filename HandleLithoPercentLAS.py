import lasio
import numpy as np
import openpyxl

from HelperFunc import resource_path, readLocalFile, writeLocalFile
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

    firstRow = ' '.join(las.keys())
    lasFilename = resource_path('draft.las')
    excelFilename = resource_path('draft.xlsx')

    las.write(lasFilename, fmt='%.0f', len_numeric_field=5)
    las.to_excel(excelFilename)

    DSG()
    LITHOLOGY()

    trimLASandEXCEL(lasFilename, excelFilename, firstRow)

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

    lasFilename = resource_path('draft_DSG.las')
    excelFilename = resource_path('draft_DSG.xlsx')
    firstRow = ' '.join(las.keys())

    las.write(lasFilename, fmt='%.0f', len_numeric_field=5)
    las.to_excel(excelFilename)
    trimLASandEXCEL(lasFilename, excelFilename, firstRow)

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

    lasFilename = resource_path('draft_LITHOLOGY.las')
    excelFilename = resource_path('draft_LITHOLOGY.xlsx')
    firstRow = ' '.join(newLas.keys())

    newLas.write(lasFilename, fmt='%.0f', len_numeric_field=5)
    newLas.to_excel(excelFilename)
    trimLASandEXCEL(lasFilename, excelFilename, firstRow)


def trimLASandEXCEL(lasFilename, excelFilename, firstRow):
    workbook = openpyxl.load_workbook(excelFilename)
    std = workbook.get_sheet_by_name('Header')
    workbook.remove_sheet(std)
    workbook.save(excelFilename)

    txt = readLocalFile(lasFilename)

    start = '~ASCII -----------------------------------------------------'
    data = txt[txt.find(start)+len(start):len(txt)-1]
    finalData = f'{firstRow}{data}'

    writeLocalFile(lasFilename, finalData)
