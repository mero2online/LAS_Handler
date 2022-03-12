from tkinter import filedialog
from tkinter import *
from tkinter import scrolledtext
import lasio
from my_const import *
from GetFunc import *
import datetime
from HelperFunc import resource_path

filetypes = (
    ('LAS files', '*.las'),
    ('All files', '*.*'),
)


def gen_litho_LAS(filename):
    las = lasio.read(filename)

    # print(las.keys())
    # LTY_remove_NaN = np.nan_to_num(LTY, copy=True)
    # volcut_anhy = [math.trunc(value) for value in LTY_remove_NaN]
    # print(las.get_curve('LTY'))
    # print(las['LTY'])

    wellNameOriginal = las.well.WELL.value
    finalWellName = wellNameOriginal[wellNameOriginal.find(
        '(')+len('('):wellNameOriginal.rfind(')')]
    las.well.WELL = finalWellName

    day = datetime.datetime.now().strftime("%d")
    month = datetime.datetime.now().strftime("%b").upper()
    year = datetime.datetime.now().strftime("%Y")
    finalWellDate = f'{day}_{month}_{year}'
    las.well.DATE = finalWellDate

    las.well.SRVC = 'EXLOG'

    LTY = las['LTY']

    VOLCUT_ANHY = GET_VOLCUT_ANHY(LTY)
    VOLCUT_ARGDOL = GET_VOLCUT_ARGDOL(LTY)
    VOLCUT_ARGLS = GET_VOLCUT_ARGLS(LTY)
    VOLCUT_CALDOL = GET_VOLCUT_CALDOL(LTY)
    VOLCUT_CALLS = GET_VOLCUT_CALLS(LTY)
    VOLCUT_CEMENT = GET_VOLCUT_CEMENT(LTY)
    VOLCUT_CHERT = GET_VOLCUT_CHERT(LTY)
    VOLCUT_CLAY = GET_VOLCUT_CLAY(LTY)
    VOLCUT_COAL = GET_VOLCUT_COAL(LTY)
    VOLCUT_CONG = GET_VOLCUT_CONG(LTY)
    VOLCUT_DOL = GET_VOLCUT_DOL(LTY)
    VOLCUT_DOLLS = GET_VOLCUT_DOLLS(LTY)
    VOLCUT_GYP = GET_VOLCUT_GYP(LTY)
    VOLCUT_HAL = GET_VOLCUT_HAL(LTY)
    VOLCUT_IGN = GET_VOLCUT_IGN(LTY)
    VOLCUT_LS = GET_VOLCUT_LS(LTY)
    VOLCUT_MARL = GET_VOLCUT_MARL(LTY)
    VOLCUT_SAND = GET_VOLCUT_SAND(LTY)
    VOLCUT_SH = GET_VOLCUT_SH(LTY)
    VOLCUT_SST = GET_VOLCUT_SST(LTY)

    las.append_curve('DEPTH', las['DMEA'],
                     unit='ft', descr='1 Hole Depth')

    las.append_curve('VOLCUT_ANHY', VOLCUT_ANHY,
                     unit='%', descr='2 Anhydrite')
    las.append_curve('VOLCUT_ARGDOL', VOLCUT_ARGDOL,
                     unit='%', descr='3 Argillaceous Dolomite')
    las.append_curve('VOLCUT_ARGLS', VOLCUT_ARGLS,
                     unit='%', descr='4 Argillaceous Limestone')
    las.append_curve('VOLCUT_CALDOL', VOLCUT_CALDOL,
                     unit='%', descr='5 Calcarenite Dolomite')
    las.append_curve('VOLCUT_CALLS', VOLCUT_CALLS,
                     unit='%', descr='6 Calcarenite Limestone')
    las.append_curve('VOLCUT_CEMENT', VOLCUT_CEMENT,
                     unit='%', descr='7 Cement')
    las.append_curve('VOLCUT_CHERT', VOLCUT_CHERT,
                     unit='%', descr='8 Chert')
    las.append_curve('VOLCUT_CLAY', VOLCUT_CLAY,
                     unit='%', descr='9 Clay')
    las.append_curve('VOLCUT_COAL', VOLCUT_COAL,
                     unit='%', descr='10 Coal_Lignite_TAR')
    las.append_curve('VOLCUT_CONG', VOLCUT_CONG,
                     unit='%', descr='11 Conglomerate')
    las.append_curve('VOLCUT_DOL', VOLCUT_DOL,
                     unit='%', descr='12 Dolomite')
    las.append_curve('VOLCUT_DOLLS', VOLCUT_DOLLS,
                     unit='%', descr='13 Dolomitic Limestone')
    las.append_curve('VOLCUT_GYP', VOLCUT_GYP,
                     unit='%', descr='14 Gypsum')
    las.append_curve('VOLCUT_HAL', VOLCUT_HAL,
                     unit='%', descr='15 Halite')
    las.append_curve('VOLCUT_IGN', VOLCUT_IGN,
                     unit='%', descr='16 Igneous')
    las.append_curve('VOLCUT_LS', VOLCUT_LS,
                     unit='%', descr='17 Limestone')
    las.append_curve('VOLCUT_MARL', VOLCUT_MARL,
                     unit='%', descr='18 Marl')
    las.append_curve('VOLCUT_SAND', VOLCUT_SAND,
                     unit='%', descr='19 Sandstone')
    las.append_curve('VOLCUT_SH', VOLCUT_SH,
                     unit='%', descr='20 Shale')
    las.append_curve('VOLCUT_SST', VOLCUT_SST,
                     unit='%', descr='21 Siltstone')

    las.delete_curve('LTY')
    las.delete_curve('DMEA')

    las.write(resource_path('draft.las'), fmt='%.0f', len_numeric_field=5)


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
