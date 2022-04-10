from tkinter import filedialog
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import asyncio
import os
import shutil

from HelperFunc import getFinalWellDate, getTimeNowText, resource_path, checkInputFile, readLocalFile, writeLocalFile
from ConvertLithoLAS import convert_Litho_LAS

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


def change_check_value():
    if (converted_checked.get() == 0):
        start_depth.set('')
        start_depth_entry.config(state="disabled")
    else:
        start_depth_entry.config(state="normal")


def convertLithoToLas():
    res = convert_Litho_LAS('LITHO')

    txt = readLocalFile(resource_path('draft.las'))
    addText(txt)

    saveBtn.config(state='normal')


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

    convert_Litho_LAS('LITHO%', str_dpt)

    txt = readLocalFile(resource_path('draft.las'))
    addText(txt)

    saveBtn.config(state='normal')


def convertROPToLas():
    convert_Litho_LAS('ROP')

    txt = readLocalFile(resource_path('draft.las'))
    addText(txt)

    saveBtn.config(state='normal')


def browseFile():
    # open-file dialog
    filename = filedialog.askopenfilename(
        title='Select a file...',
        filetypes=filetypes,)

    clearFiles()
    if (filename):
        selectedFilePath.set(filename)
        global resCheckInputFile
        resCheckInputFile = checkInputFile(filename)
        convertedCheckBtn.config(state="disabled")
        converted_checked.set(0)
        start_depth_entry.config(state="disabled")
        start_depth.set('')
        saveBtn.config(state='disabled')

        if resCheckInputFile[0] == 'LITHO':
            convertLithoBtn.config(state="normal")
            convertLithoPercentBtn.config(state="disabled")
            convertROPBtn.config(state="disabled")
            convertedCheckBtn.config(state="disabled")
            converted_checked.set(0)
            start_depth_entry.config(state="disabled")
            start_depth.set('')
        if resCheckInputFile[0] == 'LITHO%':
            convertLithoPercentBtn.config(state="normal")
            convertLithoBtn.config(state="disabled")
            convertROPBtn.config(state="disabled")
            convertedCheckBtn.config(state="normal")
        if resCheckInputFile[0] == 'ROP':
            convertROPBtn.config(state="normal")
            convertLithoPercentBtn.config(state="disabled")
            convertLithoBtn.config(state="disabled")
            convertedCheckBtn.config(state="disabled")
            converted_checked.set(0)
            start_depth_entry.config(state="disabled")
            start_depth.set('')
        if resCheckInputFile[0] == '':
            addText('')
            convertLithoBtn.config(state="disabled")
            convertLithoPercentBtn.config(state="disabled")
            convertROPBtn.config(state="disabled")
            convertedCheckBtn.config(state="disabled")
            converted_checked.set(0)
            start_depth_entry.config(state="disabled")
            start_depth.set('')
            messagebox.showerror('File error', 'Please load valid LAS file')
            selectedFilePath.set('')
            return False

        txt = readLocalFile(filename)
        addText(txt)
        writeLocalFile(resource_path('input.las'), txt)
    else:
        addText('')
        convertLithoBtn.config(state="disabled")
        convertLithoPercentBtn.config(state="disabled")
        convertROPBtn.config(state="disabled")
        convertedCheckBtn.config(state="disabled")
        converted_checked.set(0)
        start_depth_entry.config(state="disabled")
        start_depth.set('')
        selectedFilePath.set('')
        saveBtn.config(state='disabled')


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
        messagebox.showinfo(
            'Success', f'Files saved successfully to\n{dest_dir}')


async def copyFiles(src_files, dest_dir):
    os.mkdir(dest_dir)
    for file_name in src_files:
        if os.path.isfile(resource_path(f'out\\{file_name}')):
            shutil.copy(resource_path(f'out\\{file_name}'), dest_dir)


def getText():
    text = txtbox.get('1.0', END)
    return text


def addText(txt):
    txtbox.delete('1.0', END)
    txtbox.insert(INSERT, txt)


def insertText(txt):
    txtbox.insert(INSERT, txt)


def clearFiles():
    writeLocalFile(resource_path('input.las'), '')
    writeLocalFile(resource_path('draft.las'), '')
    writeLocalFile(resource_path('draft_DSG.las'), '')
    writeLocalFile(resource_path('draft_LITHOLOGY.las'), '')
    writeLocalFile(resource_path('draft.txt'), '')
    if (os.path.exists(resource_path('out'))):
        shutil.rmtree(resource_path('out\\'))
    os.mkdir(resource_path('out'))
    if (os.path.exists(resource_path('draft.xlsx'))):
        os.remove(resource_path('draft.xlsx'))
    if (os.path.exists(resource_path('draft_DSG.xlsx'))):
        os.remove(resource_path('draft_DSG.xlsx'))
    if (os.path.exists(resource_path('draft_LITHOLOGY.xlsx'))):
        os.remove(resource_path('draft_LITHOLOGY.xlsx'))


def copy_DSG_ConfigFile():
    cwd = os.getcwd()
    if os.path.exists(f'{cwd}\config.csv') == False:
        shutil.copy(resource_path('config.csv'), cwd)


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

convertROPBtn = Button(root, text="Convert ROP", background='#3c0470', foreground='#faebd7', borderwidth=2, relief="groove", padx=5, pady=5,
                       command=convertROPToLas)
convertROPBtn.place(x=110, y=5, width=100, height=35)
convertROPBtn.config(state="disabled")

convertLithoBtn = Button(root, text="Convert Litho", background='#3c0470', foreground='#faebd7', borderwidth=2, relief="groove", padx=5, pady=5,
                         command=convertLithoToLas)
convertLithoBtn.place(x=215, y=5, width=100, height=35)
convertLithoBtn.config(state="disabled")

convertLithoPercentBtn = Button(root, text="Convert Litho %", background='#3c0470', foreground='#faebd7', borderwidth=2, relief="groove", padx=5, pady=5,
                                command=convertLithoPercentToLas)
convertLithoPercentBtn.place(x=320, y=5, width=115, height=35)
convertLithoPercentBtn.config(state="disabled")

converted_checked = IntVar()
convertedCheckBtn = Checkbutton(root, text="Converted", variable=converted_checked,
                                background='#633192', pady=20, padx=20, borderwidth=2, relief="ridge", command=change_check_value)
convertedCheckBtn.place(x=440, y=5, width=100, height=35)
convertedCheckBtn.config(state="disabled")

start_depth_label = Label(root, text='Start Depth',
                          background='#633192', foreground='#faebd7')
start_depth_label.place(x=545, y=5, width=80, height=35)

start_depth = StringVar()
start_depth.trace('w', limitSizeDepth)
start_depth_entry = Entry(root, textvariable=start_depth,
                          background='#fff', borderwidth=2, relief="ridge", font=('Arial', 12, 'bold'))
start_depth_entry.place(x=630, y=5, width=55, height=35)
start_depth_entry.config(state="disabled")

saveBtn = Button(root, text="Save File", background='#633192', foreground='#faebd7', borderwidth=2, relief="raised", padx=5, pady=5,
                 command=saveFile)
saveBtn.grid(row=0, column=3, padx=5, pady=5, sticky=W)
saveBtn.config(state='disabled')

selectedFilePath = StringVar()
currentFilePath = Label(
    root, textvariable=selectedFilePath, background='#633192', foreground='#faebd7', anchor=W)
currentFilePath.grid(row=1, column=0, columnspan=4, pady=5, padx=5, sticky=E+W)

group1 = LabelFrame(root, text="LAS", padx=5, pady=5)
group1.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=E+W+N+S)

# Create the textbox
txtbox = scrolledtext.ScrolledText(group1)
txtbox.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)

root.title('LAS_Handler')
root.geometry('1100x500')
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
