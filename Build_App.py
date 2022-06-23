import PyInstaller.__main__
import os
import shutil
import platform

from HelperFunc import readLocalFile, writeLocalFile
from settings import appVersionNo

cwd = os.getcwd()
wd = f'{cwd}\\dist\\LAS_Handler'
if os.path.exists(wd):
    shutil.rmtree(wd)


def editInoFiles(filename):
    ino = readLocalFile(f'{cwd}\\dist\\{filename}.iss')

    startOne = '#define MyAppName "LAS_Handler"'
    endOne = '#define MyAppPublisher "MeRo2oNliNe, Inc."'
    textBeforeV = ino[0:ino.find(startOne)+len(startOne)]
    newVerText = f'#define MyAppVersion "{appVersionNo}"'
    textAfterV = ino[ino.rfind(endOne):]
    textToWrite = f'{textBeforeV}\n{newVerText}\n{textAfterV}'

    writeLocalFile(f'{cwd}\\dist\\{filename}.iss', textToWrite)


inoFileNameWin10 = 'LAS_Handler_Setup_Generator_Win10'
inoFileNameWin7 = 'LAS_Handler_Setup_Generator_Win7'

editInoFiles(inoFileNameWin10)
editInoFiles(inoFileNameWin7)

PyInstaller.__main__.run([
    'LAS_Handler.py',
    # '--onefile',
    '--windowed',
    '--add-data', 'src;src',
    '-i', ".\src\las.ico",
    '--splash', ".\src\las.png",
    '--exclude-module', 'matplotlib'
])

if platform.system() == 'Windows' and platform.release() == '10':
    os.system(f'start {cwd}\\dist\\{inoFileNameWin10}.iss')
elif platform.system() == 'Windows' and platform.release() == '7':
    os.system(f'start {cwd}\\dist\\{inoFileNameWin7}.iss')

os.chdir(f'{cwd}\dist')  # Change directory to run command
os.system('start.')  # Run command
