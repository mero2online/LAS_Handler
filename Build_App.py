import PyInstaller.__main__

PyInstaller.__main__.run([
    'LAS_Handler.py',
    '--onefile',
    '--windowed',
    '--add-data', 'src;src',
    '-i', ".\src\las.ico",
    '--splash', ".\src\las.png",
    '--exclude-module', 'matplotlib'
])
