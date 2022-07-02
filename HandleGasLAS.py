import lasio
import xlwt
import xlwings
import numpy as np

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

    curvesForExcel = [0, 22, 1, 4, 7, 10, 13, 16, 19]
    dataForExcel = []

    for d in curvesForExcel:
        curveName = las.keys()[d]
        dataForExcel.append(las[curveName])

    # Convert column to rows
    finalData = np.array(dataForExcel).T.tolist()

    topRow = ['DEPTH (ft)', 'TG', 'C1', 'C2', 'C3', 'iC4', 'nC4', 'iC5', 'nC5']
    finalData.insert(0, topRow)
    wb = xlwt.Workbook()
    sheet = wb.add_sheet(f'{las.well.WELL.value}')
    sheet.set_panes_frozen(True)
    sheet.set_horz_split_pos(1)
    # sheet.set_vert_split_pos(1)

    style = xlwt.easyxf('borders: top_color black, bottom_color black, right_color black, left_color black,\
                              left thin, right thin, top thin, bottom thin;\
                     align: horiz center; font: name Calibri, bold 1, height 220;', num_format_str='0')
    # font height 200: this is font with height 10 points
    sheet.col(0).width = 10*275

    for r_idx, row in enumerate(finalData):
        for c_idx, v in enumerate(row):
            sheet.write(r_idx, c_idx, v, style)
    finalFileNameXls = f'{las.well.WELL.value}_GAS_{las.well.DATE.value}_GRAVITAS'
    wb.save(resource_path(f'out\\{finalFileNameXls}.xls'))

    excel_app = xlwings.App(visible=False)
    excel_book = excel_app.books.open(
        resource_path(f'out\\{finalFileNameXls}.xls'))
    excel_book.save()
    excel_book.close()
    excel_app.quit()

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

    startThree = '        CO2_1       '
    textThreeLas = textOriginal[textOriginal.find(
        startThree)+len(startThree):len(textOriginal)-1]

    finalData = f'{text1}{textOneLas}{text10}{textTwoLas}{text11}{textThreeLas}'

    writeLocalFile(resource_path('draft.las'), finalData)

    finalFileNameLas = f'{las.well.WELL.value}_GAS_{las.well.DATE.value}'
    writeLocalFile(resource_path(f'out\\{finalFileNameLas}.las'), finalData)
