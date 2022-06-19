import PyInstaller.__main__
import os
import shutil
import platform

cwd = os.getcwd()
wd = f'{cwd}\\dist\\LAS_Handler'
if os.path.exists(wd):
    shutil.rmtree(wd)

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
    os.system(f'start {cwd}\\dist\\LAS_Handler_Setup_Generator.iss')
elif platform.system() == 'Windows' and platform.release() == '7':
    os.system(f'start {cwd}\\dist\\LAS_Handler_Setup_Generator_Win7.iss')

os.chdir(f'{cwd}\dist')  # Change directory to run command
os.system('start.')  # Run command
