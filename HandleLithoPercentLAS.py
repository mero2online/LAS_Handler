import lasio
import numpy as np
import openpyxl

from HelperFunc import resource_path
from NewCurvesData import newPerCurves
from GetFunc import convertNULL


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
