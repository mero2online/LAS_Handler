from tkinter import filedialog
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import os
import shutil

from my_const import *
from HelperFunc import resource_path, checkInputFile, readLocalFile, writeLocalFile
from ConvertLithoLAS import convert_Litho_LAS

filetypes = (
    ('LAS files', '*.las'),
    ('All files', '*.*'),
)

resCheckInputFile = ''


def convertLithoToLas():
    res = convert_Litho_LAS('LITHO')

    addText(text1)
    insertText(res.get('textOneLas'))

    insertText(text2)
    insertText(res.get('textTwoLas'))

    insertText(text3)
    insertText(res.get('textThreeLas'))

    writeOutputToFile()

    saveBtn.config(state='normal')


def convertLithoPercentToLas():
    convert_Litho_LAS('LITHO%')

    txt = readLocalFile(resource_path('draft.las'))
    addText(txt)

    saveBtn.config(state='normal')


def browseFile():
    # open-file dialog
    filename = filedialog.askopenfilename(
        title='Select a file...',
        filetypes=filetypes,)
    # root.destroy()
    clearFiles()
    if (filename):
        selectedFilePath.set(filename)
        global resCheckInputFile
        resCheckInputFile = checkInputFile(filename)

        if resCheckInputFile == 'LITHO':
            convertLithoBtn.config(state="normal")
            convertLithoPercentBtn.config(state="disabled")
        if resCheckInputFile == 'LITHO%':
            convertLithoPercentBtn.config(state="normal")
            convertLithoBtn.config(state="disabled")
        if resCheckInputFile == '':
            addText('')
            convertLithoBtn.config(state="disabled")
            convertLithoPercentBtn.config(state="disabled")
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
        selectedFilePath.set('')
        saveBtn.config(state='disabled')


def saveFile():
    # save-as dialog
    filename = filedialog.askdirectory()

    srcLAS = resource_path('draft.las')
    dstLAS = f'{filename}/{resCheckInputFile}_OUTPUT.las'
    shutil.copy(srcLAS, dstLAS)

    # make a copy of the invoice to work with
    if resCheckInputFile == 'LITHO%':
        src = resource_path('draft.xlsx')
        dst = f'{filename}/{resCheckInputFile}_OUTPUT.xlsx'
        shutil.copy(src, dst)
        src = resource_path('draft_DSG.xlsx')
        dst = f'{filename}/{resCheckInputFile}_DSG_OUTPUT.xlsx'
        shutil.copy(src, dst)
        src = resource_path('draft_DSG.las')
        dst = f'{filename}/{resCheckInputFile}_DSG_OUTPUT.las'
        shutil.copy(src, dst)
        src = resource_path('draft_LITHOLOGY.las')
        dst = f'{filename}/{resCheckInputFile}_LITHOLOGY_OUTPUT.las'
        shutil.copy(src, dst)
        src = resource_path('draft_LITHOLOGY.xlsx')
        dst = f'{filename}/{resCheckInputFile}_LITHOLOGY_OUTPUT.xlsx'
        shutil.copy(src, dst)
    # root.destroy()


def getText():
    text = txtbox.get('1.0', END)
    return text


def addText(txt):
    txtbox.delete('1.0', END)
    txtbox.insert(INSERT, txt)


def insertText(txt):
    txtbox.insert(INSERT, txt)


def writeOutputToFile():
    allText = getText()
    writeLocalFile(resource_path('draft.las'), allText)


def clearFiles():
    writeLocalFile(resource_path('input.las'), '')
    writeLocalFile(resource_path('draft.las'), '')
    writeLocalFile(resource_path('draft_DSG.las'), '')
    writeLocalFile(resource_path('draft_LITHOLOGY.las'), '')

    if (os.path.exists(resource_path('draft.xlsx'))):
        os.remove(resource_path('draft.xlsx'))
    if (os.path.exists(resource_path('draft_DSG.xlsx'))):
        os.remove(resource_path('draft_DSG.xlsx'))
    if (os.path.exists(resource_path('draft_LITHOLOGY.xlsx'))):
        os.remove(resource_path('draft_LITHOLOGY.xlsx'))


clearFiles()

root = Tk()

Button(root, text="Browse File", background='#633192', foreground='#faebd7', borderwidth=2, relief="raised", padx=5, pady=5,
       command=browseFile).grid(row=0, column=0, padx=5, pady=5, sticky=W)

convertLithoBtn = Button(root, text="Convert Litho", background='#3c0470', foreground='#faebd7', borderwidth=2, relief="groove", padx=5, pady=5,
                         command=convertLithoToLas)
convertLithoBtn.grid(row=0, column=1, padx=5, pady=5, sticky=W)
convertLithoBtn.config(state="disabled")

convertLithoPercentBtn = Button(root, text="Convert Litho %", background='#3c0470', foreground='#faebd7', borderwidth=2, relief="groove", padx=5, pady=5,
                                command=convertLithoPercentToLas)
convertLithoPercentBtn.grid(row=0, column=1, padx=105, pady=5, sticky=W)
convertLithoPercentBtn.config(state="disabled")

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
