from tkinter import *
from tkinter import messagebox
import os

from HelperFunc import resource_path, readLocalFile, writeLocalFile
import settings

cwd = os.getcwd()


def openDsgConfig():
    if settings.counter < 2:
        settings.counter += 1
        dsgConfig()
    else:
        messagebox.showerror('Error', 'Please close opened window first')


def getCSVData():
    text = readLocalFile(f'{cwd}\LAS_Handler_DSG_Config.csv')

    result = []

    for line in text.splitlines():
        result.append(line.split(",")[1])

    return result


def saveConfig(prov, long, lati, xcoord, ycoord, elev, td, saveStatusVar):
    parameters = ['PROV', 'LONG', 'LATI', 'XCOORD', 'YCOORD', 'ELEV', 'TD']
    values = [prov.get(), long.get(), lati.get(), xcoord.get(),
              ycoord.get(), elev.get(), td.get()]

    arr = []
    for idx, x in enumerate(parameters):
        arr.append(f'{x},{values[idx]}')

    txt = '\n'.join(arr)
    writeLocalFile(f'{cwd}\LAS_Handler_DSG_Config.csv', txt)
    saveStatusVar.set('DSG Config saved successfully')


def clearSaveStatusVar(saveStatusVar):
    saveStatusVar.set('')


def dsgConfig():
    app = Tk()
    saveStatusVar = StringVar(app, '')

    result = getCSVData()
    PROV, LONG, LATI, XCOORD, YCOORD, ELEV, TD = result

    prov_label = Label(app, text='PROV',
                       background='#633192', foreground='#faebd7')
    prov_label.place(x=10, y=5, width=80, height=35)

    prov = StringVar(app, value=PROV)
    prov.trace('w', lambda var, index, mode,
               sv=saveStatusVar: clearSaveStatusVar(sv))
    prov_entry = Entry(app, textvariable=prov,
                       background='#fff', borderwidth=2, relief="ridge", font=('Arial', 12, 'bold'))
    prov_entry.place(x=100, y=5, width=200, height=35)

    long_label = Label(app, text='LONG',
                       background='#633192', foreground='#faebd7')
    long_label.place(x=10, y=45, width=80, height=35)

    long = StringVar(app, value=LONG)
    long.trace('w', lambda var, index, mode,
               sv=saveStatusVar: clearSaveStatusVar(sv))
    long_entry = Entry(app, textvariable=long,
                       background='#fff', borderwidth=2, relief="ridge", font=('Arial', 12, 'bold'))
    long_entry.place(x=100, y=45, width=200, height=35)

    lati_label = Label(app, text='LATI',
                       background='#633192', foreground='#faebd7')
    lati_label.place(x=10, y=85, width=80, height=35)

    lati = StringVar(app, value=LATI)
    lati.trace('w', lambda var, index, mode,
               sv=saveStatusVar: clearSaveStatusVar(sv))
    lati_entry = Entry(app, textvariable=lati,
                       background='#fff', borderwidth=2, relief="ridge", font=('Arial', 12, 'bold'))
    lati_entry.place(x=100, y=85, width=200, height=35)

    xcoord_label = Label(app, text='XCOORD',
                         background='#633192', foreground='#faebd7')
    xcoord_label.place(x=10, y=125, width=80, height=35)

    xcoord = StringVar(app, value=XCOORD)
    xcoord.trace('w', lambda var, index, mode,
                 sv=saveStatusVar: clearSaveStatusVar(sv))
    xcoord_entry = Entry(app, textvariable=xcoord,
                         background='#fff', borderwidth=2, relief="ridge", font=('Arial', 12, 'bold'))
    xcoord_entry.place(x=100, y=125, width=200, height=35)

    ycoord_label = Label(app, text='YCOORD',
                         background='#633192', foreground='#faebd7')
    ycoord_label.place(x=10, y=165, width=80, height=35)

    ycoord = StringVar(app, value=YCOORD)
    ycoord.trace('w', lambda var, index, mode,
                 sv=saveStatusVar: clearSaveStatusVar(sv))
    ycoord_entry = Entry(app, textvariable=ycoord,
                         background='#fff', borderwidth=2, relief="ridge", font=('Arial', 12, 'bold'))
    ycoord_entry.place(x=100, y=165, width=200, height=35)

    elev_label = Label(app, text='ELEV',
                       background='#633192', foreground='#faebd7')
    elev_label.place(x=10, y=205, width=80, height=35)

    elev = StringVar(app, value=ELEV)
    elev.trace('w', lambda var, index, mode,
               sv=saveStatusVar: clearSaveStatusVar(sv))
    elev_entry = Entry(app, textvariable=elev,
                       background='#fff', borderwidth=2, relief="ridge", font=('Arial', 12, 'bold'))
    elev_entry.place(x=100, y=205, width=200, height=35)

    td_label = Label(app, text='TD',
                     background='#633192', foreground='#faebd7')
    td_label.place(x=10, y=245, width=80, height=35)

    td = StringVar(app, value=TD)
    td.trace('w', lambda var, index, mode,
             sv=saveStatusVar: clearSaveStatusVar(sv))
    td_entry = Entry(app, textvariable=td,
                     background='#fff', borderwidth=2, relief="ridge", font=('Arial', 12, 'bold'))
    td_entry.place(x=100, y=245, width=200, height=35)

    saveStatus = Label(app, textvariable=saveStatusVar,
                       background='#633192', foreground='#faebd7')
    saveStatus.place(x=25, y=330, width=250, height=20)

    saveBtn = Button(app, text="Save Config", background='#633192', foreground='#faebd7', borderwidth=2, relief="raised", padx=10, pady=5,
                     command=lambda: saveConfig(prov, long, lati, xcoord, ycoord, elev, td, saveStatusVar))
    saveBtn.place(x=25, y=290, width=250, height=35)

    app.title('DSG Config')
    app.geometry('320x360')
    app.configure(bg='#000')
    app.resizable(False, False)
    # Setting icon of master window
    app.iconbitmap(resource_path('las.ico'))

    def onClosing():
        settings.counter = 1
        app.destroy()

    app.protocol('WM_DELETE_WINDOW', onClosing)
    # Start program
    app.mainloop()
