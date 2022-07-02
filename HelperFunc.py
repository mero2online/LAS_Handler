import os
import sys
import lasio
import datetime


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, 'src\\', relative_path)


def checkInputFile(filename):
    inputFileContent = []
    try:
        las = lasio.read(filename)
        startDepth = las.well.STRT.value
        stopDepth = las.well.STOP.value
        if las.keys() == ['DMEA', 'LTY']:
            inputFileContent.append('LITHO')
        elif las.keys() == ['DMEA', 'LPT', 'CLI', 'CDO', 'LFL1', 'LFL2',
                            'UNKNOWN:1', 'UNKNOWN:2', 'UNKNOWN:3', 'UNKNOWN:4',
                            'UNKNOWN:5', 'UNKNOWN:6', 'UNKNOWN:7', 'UNKNOWN:8',
                            'UNKNOWN:9', 'UNKNOWN:10', 'UNKNOWN:11', 'UNKNOWN:12',
                            'UNKNOWN:13', 'UNKNOWN:14', 'UNKNOWN:15', 'UNKNOWN:16',
                            'UNKNOWN:17', 'UNKNOWN:18', 'UNKNOWN:19', 'UNKNOWN:20',
                            'UNKNOWN:21', 'UNKNOWN:22', 'UNKNOWN:23', 'UNKNOWN:24',
                            'UNKNOWN:25', 'UNKNOWN:26', 'UNKNOWN:27', 'UNKNOWN:28']:
            inputFileContent.append('LITHO%')
        elif las.keys() == ['DMEA', 'ROPA']:
            inputFileContent.append('ROP')
        elif all(x in las.keys() for x in ['DMEA', 'DBTM', 'HDIA', 'MFII', 'MFOI', 'MTIA', 'MTOA', 'MDIA', 'MDOA',
                                           'ROPA', 'RPMI', 'RPMTI', 'RPMMI', 'WOBI', 'HKLI', 'SPPI',
                                           'MCIA', 'MCOA', 'TVT1', 'CO2_1', 'AH2S1', 'UD1']):
            inputFileContent.append('DRILL')
        elif all(x in las.keys() for x in ['DMEA', 'METH', 'METH2', 'METH1', 'ETH', 'ETH2', 'ETH1',
                                           'PRP', 'PRP2', 'PRP1', 'IBUT', 'IBUT2', 'IBUT1',
                                           'NBUT', 'NBUT2', 'NBUT1', 'IPEN', 'IPEN2', 'IPEN1',
                                           'NPEN', 'NPEN2', 'NPEN1', 'CO2_1']) \
                and las.keys()[len(las.keys())-1] == 'CO2_1':
            inputFileContent.append('GAS')
        else:
            inputFileContent.append('')

        inputFileContent.append(startDepth)
        inputFileContent.append(stopDepth)
    except KeyError:
        pass
    return inputFileContent


def readLocalFile(filename):
    f = open(filename, 'r')
    txt = f.read()
    f.close()

    return txt


def writeLocalFile(filename, txt):
    f = open(filename, 'w')
    f.write(txt)
    f.close()


def getFinalWellDate():
    day = datetime.datetime.now().strftime("%d")
    month = datetime.datetime.now().strftime("%b").upper()
    year = datetime.datetime.now().strftime("%Y")
    return f'{day}_{month}_{year}'


def getTimeNowText():
    time = datetime.datetime.now()
    return f'{time.hour}_{time.minute}_{time.second}'
