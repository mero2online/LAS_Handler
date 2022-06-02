import PyInstaller.__main__
import os
import shutil

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

os.system(f'start {cwd}\\dist\\LAS_Handler_Setup_Generator.iss')

os.chdir(f'{cwd}\dist')  # Change directory to run command
os.system('start.')  # Run command
