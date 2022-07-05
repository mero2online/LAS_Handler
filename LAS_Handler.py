from tkinter import filedialog
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import asyncio
import os
import shutil

from HelperFunc import getFinalWellDate, getTimeNowText, resource_path, checkInputFile, readLocalFile, writeLocalFile
from ConvertLithoLAS import convert_Litho_LAS
from DSG_CONFIG_WINDOW import openDsgConfig
import settings
from settings import appVersionNo

try:
    import pyi_splash  # type: ignore
    pyi_splash.close()
except:
    pass

filetypes = (
    ('LAS files', '*.las'),
    ('All files', '*.*'),
)

resCheckInputFile = []
settings.init()


def change_check_value():
    if (converted_checked.get() == 0):
        start_depth.set('')
        start_depth_entry.config(state="disabled")
    else:
        start_depth_entry.config(state="normal")


def showLoading():
    disableAllButtonsExcept('')
    addText('\n........')
    for i in range(16):
        insertText('........')
    insertText(' Loading ')
    for i in range(16):
        insertText('........')
    root.update()


def showSuccessMsg():
    messagebox.showinfo('Success', f'File converted successfully')


def convertLithoToLas():
    showLoading()
    convert_Litho_LAS('LITHO')

    txt = readLocalFile(resource_path('draft.las'))
    addText(txt)
    showSuccessMsg()

    saveBtn.config(state='normal')
    explorationCheckBtn.config(state='normal')


def convertLithoPercentToLas():
    cnv_ckd = converted_checked.get()
    str_dpt = start_depth.get()
    las_str_dpt = int(resCheckInputFile[1])

    if (cnv_ckd == 0 and os.path.exists(resource_path('out'))):
        shutil.rmtree(resource_path('out\\'))
        os.mkdir(resource_path('out'))

    if cnv_ckd == 1:
        if str_dpt == '':
            messagebox.showerror('Error', 'Start Depth Can\'t be empty')
            return

        if int(str_dpt) > las_str_dpt:
            messagebox.showerror(
                'Error', f'Start Depth Can\'t be Large than LAS START\n{str_dpt}>{las_str_dpt}')
            return

        if int(str_dpt) == las_str_dpt:
            messagebox.showerror(
                'Error', f'Start Depth Can\'t be same as LAS START\n{str_dpt}={las_str_dpt}')
            return

    showLoading()
    convert_Litho_LAS('LITHO%', str_dpt)

    txt = readLocalFile(resource_path('draft.las'))
    addText(txt)
    showSuccessMsg()

    saveBtn.config(state='normal')
    explorationCheckBtn.config(state='normal')


def convertROPToLas():
    showLoading()
    convert_Litho_LAS('ROP')

    txt = readLocalFile(resource_path('draft.las'))
    addText(txt)
    showSuccessMsg()

    saveBtn.config(state='normal')
    explorationCheckBtn.config(state='normal')


def convertDRILLToLas():
    showLoading()
    convert_Litho_LAS('DRILL')

    txt = readLocalFile(resource_path('draft.las'))
    addText(txt)
    showSuccessMsg()

    saveBtn.config(state='normal')
    explorationCheckBtn.config(state='normal')


def convertGASToLas():
    showLoading()
    convert_Litho_LAS('GAS')

    txt = readLocalFile(resource_path('draft.las'))
    addText(txt)
    showSuccessMsg()

    saveBtn.config(state='normal')
    explorationCheckBtn.config(state='normal')


def browseFile():
    if (settings.counter > 1):
        messagebox.showerror('Error', 'Please close DSG Config window first')
        return
    # open-file dialog
    filename = filedialog.askopenfilename(
        title='Select a file...',
        filetypes=filetypes,)

    clearFiles()
    if (filename):
        global resCheckInputFile
        resCheckInputFile = checkInputFile(filename)
        disableAllButtonsExcept('')

        if resCheckInputFile[0] == 'LITHO':
            disableAllButtonsExcept([convertLithoBtn])
        if resCheckInputFile[0] == 'LITHO%':
            disableAllButtonsExcept(
                [convertLithoPercentBtn, convertedCheckBtn, dsgConfigBtn])
        if resCheckInputFile[0] == 'ROP':
            disableAllButtonsExcept([convertROPBtn])
        if resCheckInputFile[0] == 'DRILL':
            disableAllButtonsExcept([convertDRILLBtn])
        if resCheckInputFile[0] == 'GAS':
            disableAllButtonsExcept([convertGASBtn])
        if resCheckInputFile[0] == '':
            addText('')
            disableAllButtonsExcept('')
            messagebox.showerror('File error', 'Please load valid LAS file')
            return False
        selectedFilePath.set(filename)
        txt = readLocalFile(filename)
        addText(txt)
        writeLocalFile(resource_path('input.las'), txt)
    else:
        addText('')
        disableAllButtonsExcept('')


def disableAllButtonsExcept(btn):
    allBtnS = [convertLithoBtn, convertLithoPercentBtn, convertROPBtn,
               convertDRILLBtn, convertGASBtn, convertedCheckBtn,
               dsgConfigBtn, start_depth_entry, saveBtn,
               start_depth, selectedFilePath, converted_checked,
               exploration_checked, explorationCheckBtn]

    for i, x in enumerate(allBtnS):
        if type(x) == IntVar:
            x.set(0)
        elif type(x) == StringVar:
            x.set('')
        else:
            x.config(state="disabled")

    if btn != '':
        for i, b in enumerate(btn):
            b.config(state="normal")


def saveFile():
    # save-as dialog
    filename = filedialog.askdirectory()
    asyncio.run(saveAllFiles(filename))


async def saveAllFiles(filename):
    if (filename):
        date = getFinalWellDate()
        time = getTimeNowText()
        src_files = os.listdir(resource_path('out\\'))
        dest_dir = f'{filename}/LAS-Handler-Output-{date}-{time}'
        await copyFiles(src_files, dest_dir)
        result = messagebox.askquestion(
            'Success', f'Files saved successfully to\n\n{dest_dir}\n\nOpen output folder?')
        if result == 'yes':
            opd = os.getcwd()  # Get original directory
            os.chdir(dest_dir)  # Change directory to run command
            os.system('start.')  # Run command
            os.chdir(opd)  # Return to original directory


async def copyFiles(src_files, dest_dir):
    os.mkdir(dest_dir)
    for file_name in src_files:
        newFileName = file_name.replace(
            'GRAVITAS', 'GRAFIT') if exploration_checked.get() == 1 else file_name.replace(
            'GRAFIT', 'GRAVITAS')
        os.rename(resource_path(f'out\\{file_name}'),
                  resource_path(f'out\\{newFileName}'))
        if os.path.isfile(resource_path(f'out\\{newFileName}')):
            shutil.copy(resource_path(f'out\\{newFileName}'), dest_dir)


def getText():
    text = txtbox.get('1.0', END)
    return text


def addText(txt):
    txtbox.config(state="normal")
    txtbox.delete('1.0', END)
    txtbox.insert(INSERT, txt)
    txtbox.config(state="disabled")


def insertText(txt):
    txtbox.config(state="normal")
    txtbox.insert(INSERT, txt)
    txtbox.config(state="disabled")


def clearFiles():
    lasFileNames = ['input.las', 'draft.las', 'draft_DSG.las', 'draft_LITHOLOGY.las',
                    'draft_lithology_draft.las', 'draft.txt']
    for x in lasFileNames:
        writeLocalFile(resource_path(x), '')

    xlsxFileNames = ['draft.xlsx', 'draft_DSG.xlsx', 'draft_LITHOLOGY.xlsx']
    for x in xlsxFileNames:
        if (os.path.exists(resource_path(x))):
            os.remove(resource_path(x))

    if (os.path.exists(resource_path('out'))):
        shutil.rmtree(resource_path('out\\'))
    os.mkdir(resource_path('out'))


def copy_DSG_ConfigFile():
    cwd = os.getcwd()
    if os.path.exists(f'{cwd}\LAS_Handler_DSG_Config.csv') == False:
        shutil.copy(resource_path('LAS_Handler_DSG_Config.csv'), cwd)


clearFiles()
copy_DSG_ConfigFile()


def limitSizeDepth(*args):
    value = start_depth.get()
    if len(value) > 5:
        start_depth.set(value[:5])


root = Tk()

browseBtn = Button(root, text="Browse File", background='#633192', foreground='#faebd7', borderwidth=2, relief="raised", padx=5, pady=5,
                   command=browseFile)
browseBtn.place(x=5, y=5, width=100, height=37)

btnNamesTxt = [
    "Convert DRILL", "Convert GAS", "Convert ROP", "Convert Litho", "Convert Litho %"
]
btnFunc = [
    convertDRILLToLas, convertGASToLas, convertROPToLas,
    convertLithoToLas, convertLithoPercentToLas
]
myBtnArr = []
for i in range(5):
    btn = Button(root, text=btnNamesTxt[i], background='#3c0470', foreground='#faebd7',
                 borderwidth=2, relief="groove", padx=5, pady=5,
                 command=btnFunc[i])
    xPlace = (i*105)+110
    wPlace = 115 if i == 4 else 100
    btn.place(x=xPlace, y=5, width=wPlace, height=35)
    btn.config(state="disabled")
    myBtnArr.append(btn)

convertDRILLBtn, convertGASBtn, convertROPBtn, convertLithoBtn, convertLithoPercentBtn = myBtnArr

converted_checked = IntVar()
convertedCheckBtn = Checkbutton(root, text="Converted", variable=converted_checked,
                                background='#633192', pady=20, padx=20, borderwidth=2,
                                relief="ridge", command=change_check_value)
convertedCheckBtn.place(x=650, y=5, width=100, height=35)
convertedCheckBtn.config(state="disabled")

exploration_checked = IntVar()
explorationCheckBtn = Checkbutton(root, text="Exploration", variable=exploration_checked,
                                  background='#633192', pady=20, padx=20, borderwidth=2,
                                  relief="ridge")
explorationCheckBtn.place(x=990, y=5, width=100, height=35)
explorationCheckBtn.config(state="disabled")

start_depth_label = Label(root, text='Start Depth',
                          background='#633192', foreground='#faebd7')
start_depth_label.place(x=760, y=5, width=80, height=35)

start_depth = StringVar()
start_depth.trace('w', limitSizeDepth)
start_depth_entry = Entry(root, textvariable=start_depth,
                          background='#fff', borderwidth=2, relief="ridge", font=('Arial', 12, 'bold'))
start_depth_entry.place(x=845, y=5, width=55, height=35)
start_depth_entry.config(state="disabled")

dsgConfigBtn = Button(root, text="DSG Config", background='#633192', foreground='#faebd7', borderwidth=2, relief="raised", padx=5, pady=5,
                      command=openDsgConfig)
dsgConfigBtn.place(x=910, y=5, width=70, height=35)
# dsgConfigBtn.config(state='disabled')

saveBtn = Button(root, text="Save File", background='#633192', foreground='#faebd7', borderwidth=2, relief="raised", padx=5, pady=5,
                 command=saveFile)
saveBtn.grid(row=0, column=3, padx=5, pady=5, sticky=W)
saveBtn.config(state='disabled')

selectedFilePath = StringVar()
currentFilePath = Label(
    root, textvariable=selectedFilePath, background='#633192', foreground='#faebd7', anchor=W)
currentFilePath.grid(row=1, column=0, columnspan=4, pady=5, padx=5, sticky=E+W)

group1 = LabelFrame(root, text="LAS", padx=5, pady=5,
                    background='#633192', foreground='#faebd7')
group1.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=E+W+N+S)

# Create the textbox
txtbox = scrolledtext.ScrolledText(group1, font=('monospace', 10, 'bold'))
txtbox.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)

madeWithLoveBy = Label(
    group1, text='Made with ❤ by Mohamed Omar', background='#633192', foreground='#faebd7',
    font=('monospace', 9, 'bold'))
madeWithLoveBy.grid(row=1, column=1, padx=5, pady=5, sticky=W)

versionNo = Label(
    group1, text=f'v.{appVersionNo}', background='#633192', foreground='#faebd7',
    font=('monospace', 9, 'bold'))
versionNo.grid(row=1, column=2, padx=5, pady=5, sticky=W)

root.title('LAS_Handler')
root.geometry('1180x500')
root.configure(bg='#000')
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(2, weight=1)
group1.grid_columnconfigure(0, weight=1)
group1.grid_rowconfigure(0, weight=1)
# root.resizable(False, False)
# Setting icon of master window
root.iconbitmap(resource_path('las.ico'))
# Start program
root.mainloop()
