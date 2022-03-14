from tkinter import filedialog
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

from my_const import *
from HelperFunc import resource_path, checkInputFile
from ConvertLithoLAS import convert_Litho_LAS

filetypes = (
    ('LAS files', '*.las'),
    ('All files', '*.*'),
)


def convertLithoToLas():
    res = convert_Litho_LAS('LITHO')

    addText(text1)
    insertText(res.get('textOneLas'))

    insertText(text2)
    insertText(res.get('textTwoLas'))

    insertText(text3)
    insertText(res.get('textThreeLas'))


def convertLithoPercentToLas():
    res = convert_Litho_LAS('LITHO%')

    addText(text4)
    insertText(res.get('textThreeLas'))


def browseFile():
    # open-file dialog
    filename = filedialog.askopenfilename(
        title='Select a file...',
        filetypes=filetypes,)
    # root.destroy()
    selectedFilePath.set(filename)
    clearFiles()
    res = checkInputFile(filename)

    if res == 'LITHO':
        convertLithoBtn.config(state="normal")
        convertLithoPercentBtn.config(state="disabled")
    if res == 'LITHO%':
        convertLithoPercentBtn.config(state="normal")
        convertLithoBtn.config(state="disabled")
    if res == '':
        addText('')
        convertLithoBtn.config(state="disabled")
        convertLithoPercentBtn.config(state="disabled")
        messagebox.showerror('File error', 'Please load valid LAS file')
        selectedFilePath.set('')
        return False
    f = open(filename, 'r')
    txt = f.read()
    f.close()
    addText(txt)

    f = open(resource_path('input.las'), 'w')
    f.write(txt)
    f.close()


def saveFile():
    # save-as dialog
    filename = filedialog.asksaveasfilename(
        title='Save as...',
        filetypes=filetypes,
        defaultextension='.las', initialfile='output'
    )
    allText = getText()
    f = open(filename, 'w')
    f.write(allText)
    f.close()
    # root.destroy()


def getText():
    text = txtbox.get('1.0', END)
    return text


def addText(txt):
    txtbox.delete('1.0', END)
    txtbox.insert(INSERT, txt)


def insertText(txt):
    txtbox.insert(INSERT, txt)


def clearFiles():
    f = open(resource_path('input.las'), 'w')
    f.close()
    f = open(resource_path('draft.las'), 'w')
    f.close()


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

Button(root, text="Save File", background='#633192', foreground='#faebd7', borderwidth=2, relief="raised", padx=5, pady=5,
       command=saveFile).grid(row=0, column=3, padx=5, pady=5, sticky=W)

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
