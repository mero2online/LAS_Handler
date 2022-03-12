import lasio
import datetime

from GetFunc import *
from HelperFunc import resource_path

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

    VOLCUT_ANHY = GET_VOLCUT_ANHY(LTY)
    VOLCUT_ARGDOL = GET_VOLCUT_ARGDOL(LTY)
    VOLCUT_ARGLS = GET_VOLCUT_ARGLS(LTY)
    VOLCUT_CALDOL = GET_VOLCUT_CALDOL(LTY)
    VOLCUT_CALLS = GET_VOLCUT_CALLS(LTY)
    VOLCUT_CEMENT = GET_VOLCUT_CEMENT(LTY)
    VOLCUT_CHERT = GET_VOLCUT_CHERT(LTY)
    VOLCUT_CLAY = GET_VOLCUT_CLAY(LTY)
    VOLCUT_COAL = GET_VOLCUT_COAL(LTY)
    VOLCUT_CONG = GET_VOLCUT_CONG(LTY)
    VOLCUT_DOL = GET_VOLCUT_DOL(LTY)
    VOLCUT_DOLLS = GET_VOLCUT_DOLLS(LTY)
    VOLCUT_GYP = GET_VOLCUT_GYP(LTY)
    VOLCUT_HAL = GET_VOLCUT_HAL(LTY)
    VOLCUT_IGN = GET_VOLCUT_IGN(LTY)
    VOLCUT_LS = GET_VOLCUT_LS(LTY)
    VOLCUT_MARL = GET_VOLCUT_MARL(LTY)
    VOLCUT_SAND = GET_VOLCUT_SAND(LTY)
    VOLCUT_SH = GET_VOLCUT_SH(LTY)
    VOLCUT_SST = GET_VOLCUT_SST(LTY)

    las.append_curve('DEPTH', las['DMEA'],
                     unit='ft', descr='1 Hole Depth')

    las.append_curve('VOLCUT_ANHY', VOLCUT_ANHY,
                     unit='%', descr='2 Anhydrite')
    las.append_curve('VOLCUT_ARGDOL', VOLCUT_ARGDOL,
                     unit='%', descr='3 Argillaceous Dolomite')
    las.append_curve('VOLCUT_ARGLS', VOLCUT_ARGLS,
                     unit='%', descr='4 Argillaceous Limestone')
    las.append_curve('VOLCUT_CALDOL', VOLCUT_CALDOL,
                     unit='%', descr='5 Calcarenite Dolomite')
    las.append_curve('VOLCUT_CALLS', VOLCUT_CALLS,
                     unit='%', descr='6 Calcarenite Limestone')
    las.append_curve('VOLCUT_CEMENT', VOLCUT_CEMENT,
                     unit='%', descr='7 Cement')
    las.append_curve('VOLCUT_CHERT', VOLCUT_CHERT,
                     unit='%', descr='8 Chert')
    las.append_curve('VOLCUT_CLAY', VOLCUT_CLAY,
                     unit='%', descr='9 Clay')
    las.append_curve('VOLCUT_COAL', VOLCUT_COAL,
                     unit='%', descr='10 Coal_Lignite_TAR')
    las.append_curve('VOLCUT_CONG', VOLCUT_CONG,
                     unit='%', descr='11 Conglomerate')
    las.append_curve('VOLCUT_DOL', VOLCUT_DOL,
                     unit='%', descr='12 Dolomite')
    las.append_curve('VOLCUT_DOLLS', VOLCUT_DOLLS,
                     unit='%', descr='13 Dolomitic Limestone')
    las.append_curve('VOLCUT_GYP', VOLCUT_GYP,
                     unit='%', descr='14 Gypsum')
    las.append_curve('VOLCUT_HAL', VOLCUT_HAL,
                     unit='%', descr='15 Halite')
    las.append_curve('VOLCUT_IGN', VOLCUT_IGN,
                     unit='%', descr='16 Igneous')
    las.append_curve('VOLCUT_LS', VOLCUT_LS,
                     unit='%', descr='17 Limestone')
    las.append_curve('VOLCUT_MARL', VOLCUT_MARL,
                     unit='%', descr='18 Marl')
    las.append_curve('VOLCUT_SAND', VOLCUT_SAND,
                     unit='%', descr='19 Sandstone')
    las.append_curve('VOLCUT_SH', VOLCUT_SH,
                     unit='%', descr='20 Shale')
    las.append_curve('VOLCUT_SST', VOLCUT_SST,
                     unit='%', descr='21 Siltstone')

    las.delete_curve('LTY')
    las.delete_curve('DMEA')

    las.write(resource_path('draft.las'), fmt='%.0f', len_numeric_field=5)
