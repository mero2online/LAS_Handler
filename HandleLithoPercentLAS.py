import lasio
import datetime
import openpyxl
from openpyxl import Workbook
from pandas import DataFrame
from openpyxl.utils.dataframe import dataframe_to_rows

from my_const import *
from HelperFunc import resource_path, readLocalFile, writeLocalFile
from NewCurvesData import newPerCurves, newPerLithCurves, modPerCurves
from GetFunc import convertNULL, GET_LITHO_EMPTY, Get_DSG_Formula


def gen_litho_Percent_LAS(filename):
    las = lasio.read(filename)

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
    csvFilename = resource_path('draft.txt')

    las.write(lasFilename, fmt='%.0f', len_numeric_field=5)
    las.to_excel(excelFilename)
    las.to_csv(csvFilename, units=False, delimiter='\t')
    csvDraft = readLocalFile(csvFilename)
    csvDraftWitoutDecimal= csvDraft.replace('.0', '')
    writeLocalFile(resource_path(f'out\\DSG_FOR_GRAVITAS_CONVERTER.txt'), csvDraftWitoutDecimal)

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
        elif (idx == 27):
            data = las[x]
            las.delete_curve(x)
            las.insert_curve(26, x, data)

    for idx, x in enumerate(las.keys()):
        if (idx == 9 or idx == 10 or idx == 16 or idx == 25):
            las.delete_curve(x)

    lasFilename = resource_path('draft_DSG.las')
    excelFilename = resource_path('draft_DSG.xlsx')

    las.to_excel(excelFilename)

    for idx, x in enumerate(las.keys()):
        if (idx > 1):
            data = las[x]+las[las.keys()[idx-1]]
            las.delete_curve(x)
            las.insert_curve(idx, x, data)

    las.insert_curve(1, 'Depth.org', las['DEPTH'])
    las.write(lasFilename, fmt='%.0f', len_numeric_field=5)
    firstRow = ' '.join(las.keys())
    trimLASandEXCEL(lasFilename, excelFilename, firstRow)

    workbook = openpyxl.load_workbook(excelFilename)
    workbook.create_sheet(title="LITHOLOGY-DSG")
    ws = workbook['Curves']
    ws.title = 'original values'
    ws1 = workbook['original values']
    ws2 = workbook['LITHOLOGY-DSG']
    df = DataFrame(ws1.values)
    rows = dataframe_to_rows(df, index=False, header=False)
    for r_idx, row in enumerate(rows, 1):
        for c_idx, value in enumerate(row, 1):
            values = Get_DSG_Formula(r_idx)
            ws2.cell(row=r_idx, column=c_idx,
                     value=value if r_idx == 1 else values[c_idx-1])

    ws2.insert_cols(2, 1)
    for x in range(len(ws1['A'])):
        i = x+1
        if x == 0:
            ws2[f'B{i}'] = 'Depth.org'
        else:
            ws2[f'B{i}'] = f'=A{i}'

    finalFileName = f'{las.well.WELL.value}_LITHOLOGY-DSG_{las.well.DATE.value}'
    # workbook.save(excelFilename)
    workbook.save(resource_path(f'out\\{finalFileName}.xlsx'))

    finalData = readLocalFile(lasFilename)
    writeLocalFile(resource_path(f'out\\{finalFileName}.las'), finalData)

#
# LITHOLOGY
#


def LITHOLOGY():
    las = lasio.read(resource_path('draft.las'))
    newLas = lasio.LASFile()
    newLas.add_curve('DEPTH', las['DEPTH'], unit='ft', descr='1 Hole Depth')

    for idx, x in enumerate(newPerLithCurves):
        if idx <= 19:
            newLas.add_curve(newPerLithCurves[idx]['name'], las[modPerCurves[idx]],
                             unit='%', descr=newPerLithCurves[idx]['desc'])
        else:
            newLas.add_curve(newPerLithCurves[idx]['name'], GET_LITHO_EMPTY(
                las['DEPTH']), unit='%', descr=newPerLithCurves[idx]['desc'])

    lasFilename = resource_path('draft_LITHOLOGY.las')
    excelFilename = resource_path('draft_LITHOLOGY.xlsx')
    firstRow = ' '.join(newLas.keys())

    newLas.write(lasFilename, fmt='%.0f', len_numeric_field=5)
    newLas.to_excel(excelFilename)

    txt = readLocalFile(resource_path('draft.las'))
    startOne = '~Well ------------------------------------------------------'
    endOne = '~Curve Information -----------------------------------------'
    textOneLas = txt[txt.find(startOne)+len(startOne):txt.rfind(endOne)]
    lith = readLocalFile(resource_path('draft_LITHOLOGY.las'))
    startTwo = '~Curve Information -----------------------------------------'
    endTwo = '~Params ----------------------------------------------------'
    textTwoLas = lith[lith.find(startTwo)+len(startTwo):lith.rfind(endTwo)]
    startThree = '~ASCII -----------------------------------------------------'
    textThreeLas = lith[lith.find(startThree)+len(startThree):len(lith)-1]
    finalData = f'{text1}{textOneLas}{text4}{textTwoLas}{text5}{textThreeLas}'

    finalFileName = f'{las.well.WELL.value}_LITHOLOGY_{las.well.DATE.value}'
    writeLocalFile(resource_path(f'out\\{finalFileName}.las'), finalData)

    wb = Workbook()
    ws1 = wb.active
    data = finalData.splitlines()
    for idx, row in enumerate(data):
        if idx <= 55:
            ws1.append([row])
        elif idx == 56:
            one = row.split()
            two = one[2:len(one)]
            two.insert(0, ' '.join([one[0], one[1]]))
            ws1.append(two)
        else:
            ws1.append([int(x) for x in row.split()])

    wb.save(resource_path(f'out\\{finalFileName}.xlsx'))

    trimLASandEXCEL(lasFilename, excelFilename, firstRow)


# ########
# Helper #
# ########


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
