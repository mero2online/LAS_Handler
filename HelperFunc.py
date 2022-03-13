import os
import sys
import lasio


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, 'src\\', relative_path)


def checkInputFile(filename):
    inputFileContent = ''
    try:
        las = lasio.read(filename)
        if las.keys() == ['DMEA', 'LTY']:
            inputFileContent = 'LITHO'

        if las.keys() == ['DMEA', 'LPT', 'CLI', 'CDO', 'LFL1', 'LFL2', 'UNKNOWN:1', 'UNKNOWN:2', 'UNKNOWN:3', 'UNKNOWN:4', 'UNKNOWN:5', 'UNKNOWN:6', 'UNKNOWN:7', 'UNKNOWN:8', 'UNKNOWN:9', 'UNKNOWN:10', 'UNKNOWN:11', 'UNKNOWN:12',
                          'UNKNOWN:13', 'UNKNOWN:14', 'UNKNOWN:15', 'UNKNOWN:16', 'UNKNOWN:17', 'UNKNOWN:18', 'UNKNOWN:19', 'UNKNOWN:20', 'UNKNOWN:21', 'UNKNOWN:22', 'UNKNOWN:23', 'UNKNOWN:24', 'UNKNOWN:25', 'UNKNOWN:26', 'UNKNOWN:27', 'UNKNOWN:28']:
            inputFileContent = 'LITHO%'
    except KeyError:
        pass
    return inputFileContent
