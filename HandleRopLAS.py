import lasio
from openpyxl import Workbook
from openpyxl.styles import Border, Side, Alignment, Font

from my_const import *
from GetFunc import *
from HelperFunc import getFinalWellDate, resource_path, readLocalFile, writeLocalFile


def gen_ROP_LAS(filename):
    las = lasio.read(filename)

    wellNameOriginal = las.well.WELL.value
    finalWellName = wellNameOriginal[wellNameOriginal.find(
        '(')+len('('):wellNameOriginal.rfind(')')]
    las.well.WELL = finalWellName

    finalWellDate = getFinalWellDate()
    las.well.DATE = finalWellDate

    las.well.SRVC = 'EXLOG'

    las.append_curve('DEPTH', aggregate_DEPTH_FiveFeet(las['DMEA']),
                     unit='FT', descr='Depth')

    las.append_curve('ROP5_ML', aggregate_ROP_FiveFeet(las['ROPA']),
                     unit='MIN/5FT', descr='Rate Of Penetration')

    las.delete_curve('DMEA')
    las.delete_curve('ROPA')

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

    finalData = f'{text1}{textOneLas}{text6}{textTwoLas}{text7}{textThreeLas}'

    writeLocalFile(resource_path('draft.las'), finalData)

    finalFileName = f'{las.well.WELL.value}_ROP-DSG_{las.well.DATE.value}'
    writeLocalFile(resource_path(f'out\\{finalFileName}.las'), finalData)

    wb = Workbook()
    ws1 = wb.active
    data = finalData.splitlines()
    ws1.append(['Depth (ft)', 'ROP (min/5 ft)'])

    for idx, row in enumerate(data):
        if idx > 33:
            ws1.append([int(x) for x in row.split()])

    columnToStyle = ['A', 'B']

    ws1.column_dimensions['A'].width = 15
    ws1.column_dimensions['B'].width = 18

    ws1.row_dimensions[1].height = 27

    topCellFont = Font(size=14, bold=True)
    cellFont = Font(bold=True)

    borderStyle = Side(border_style='thin', color='000000')
    borderPosition = Border(
        left=borderStyle, right=borderStyle, top=borderStyle, bottom=borderStyle)

    cellAlignment = Alignment(horizontal='center', vertical='center')

    for col in columnToStyle:
        for idx, cell in enumerate(ws1[col]):
            cell.font = topCellFont if idx == 0 else cellFont
            cell.border = borderPosition
            cell.alignment = cellAlignment

    ws1.freeze_panes = ws1['A2']

    wb.save(resource_path(f'out\\{finalFileName}.xlsx'))
