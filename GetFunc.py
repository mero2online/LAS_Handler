import numpy as np


def GET_VOLCUT_ANHY(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 2:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_ARGDOL(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 300:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_ARGLS(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 301:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_CALDOL(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 302:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_CALLS(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 304:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_CEMENT(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 300:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_CHERT(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        arr[x] = 0
    return arr


def GET_VOLCUT_CLAY(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 17:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_COAL(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 14:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_CONG(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 5:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_DOL(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 4:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_DOLLS(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 11:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_GYP(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        arr[x] = 0
    return arr


def GET_VOLCUT_HAL(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        arr[x] = 0
    return arr


def GET_VOLCUT_IGN(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        arr[x] = 0
    return arr


def GET_VOLCUT_LS(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 12:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_MARL(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 99:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_SAND(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 20:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_SH(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 17:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr


def GET_VOLCUT_SST(litho):
    arr = np.nan_to_num(litho, copy=True)
    for x in range(len(arr)):
        if arr[x] == 19:
            arr[x] = 100
        else:
            arr[x] = 0
    return arr
