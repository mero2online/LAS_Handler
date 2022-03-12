from tkinter import filedialog
from tkinter import *
from tkinter import scrolledtext
from my_const import *

from HelperFunc import resource_path
from HandleLithoLAS import gen_litho_LAS

filetypes = (
    ('LAS files', '*.las'),
    ('All files', '*.*'),
)


def convertLithoToLas():
    gen_litho_LAS(resource_path('input.las'))

    f = open(resource_path('draft.las'), 'r')
    txt = f.read()
    f.close()

    startOne = '~Well ------------------------------------------------------'
    endOne = '~Curve Information -----------------------------------------'
    textOneLas = txt[txt.find(startOne)+len(startOne):txt.rfind(endOne)]
    startTwo = '~Curve Information -----------------------------------------'
    endTwo = '~Params ----------------------------------------------------'
    textTwoLas = txt[txt.find(startTwo)+len(startTwo):txt.rfind(endTwo)]
    startThree = '~ASCII -----------------------------------------------------'
    textThreeLas = txt[txt.find(startThree)+len(startThree):len(txt)-1]

    addText(text1())
    txtbox.insert(INSERT, textOneLas)

    txtbox.insert(INSERT, text2())
    txtbox.insert(INSERT, textTwoLas)

    txtbox.insert(INSERT, text3())
    txtbox.insert(INSERT, textThreeLas)


def browseFile():
    # open-file dialog
    filename = filedialog.askopenfilename(
        title='Select a file...',
        filetypes=filetypes,)
    # root.destroy()

    f = open(resource_path('input.las'), 'w')
    f.close()
    f = open(resource_path('draft.las'), 'w')
    f.close()

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


root = Tk()

Button(root, text="Browse File", background='#e00707',
       command=browseFile).grid(row=0, column=0)

Button(root, text="Save File", background='#e00707',
       command=saveFile).grid(row=0, column=1)

Button(root, text="Get Text", background='#e00707',
       command=getText).grid(row=0, column=2)

Button(root, text="Convert", background='#e00707',
       command=convertLithoToLas).grid(row=0, column=3)


group1 = LabelFrame(root, text="Text Box", padx=5, pady=5)
group1.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=E+W+N+S)

# Create the textbox
txtbox = scrolledtext.ScrolledText(group1, width=130)
txtbox.grid(row=1, column=0, columnspan=4, sticky=E+W+N+S)

root.title('LAS_Handler')
root.geometry('1100x500')
root.configure(bg='#000')
root.resizable(False, False)
# Setting icon of master window
root.iconbitmap(resource_path('las.ico'))
# Start program
root.mainloop()
