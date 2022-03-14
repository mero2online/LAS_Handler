import numpy as np


def GET_LITHO_DATA(litho, lithoValue):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == lithoValue:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_LITHO_EMPTY(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        arr[x] = 0
    return arr


def convertNULL(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == -999.2500:
            arr[x] = 0
        else:
            arr[x] = arr[x]
    return arr
