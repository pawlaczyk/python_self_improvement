#coding=utf-8
import Tkinter
import PyPDF2
import StringIO
import wx
import main2
import excelTabels
import htmlTabels
import latexPDF
import os
from datetime import date
import main2
import tkMessageBox

import NessusVulnerabilities
from shutil import copyfile
import baseVulnerability

raportDate = main2.returnDate()

nameRaport = 'NazwaRaportu'
nameFirm = 'NazwaFirmy'
from os.path import expanduser
home = expanduser("~")
pathProgram = os.getcwd()
#dir is not keyword
def makemydir(name):
    try:
        os.makedirs(name)
    except OSError:
        pass

    os.chdir(name)

def chooseDate():
    top = Tkinter.Tk()

    def helloCallBack():
        l= Tkinter.Listbox( height=10)

    B = Tkinter.Button(top, text="Hello", command=helloCallBack)

    B.pack()
    top.mainloop()

def openNmapFile(path):
    nazwa = str(path).split("\\")
    nazwa = nazwa[-1]
    nazwa  = nazwa.split('.')[0]
    nameRaport = nazwa
    createFolders()
    wynikowy = main2.cutTopDown(path)
    main2.filtrFile(wynikowy)
    listOfBlocks, dataRaportu, godzinaRaportu, hostUp, liczbaHostowWSieci = main2.main()
    k = excelTabels.writeToExcel(listOfBlocks, str(nazwa))
    htmlTabels.createScheme(str(nazwa)+".html")
    data = latexPDF.returnData(listOfBlocks)
    latexPDF.createTable(data, str(nazwa), nameRaport)
    getVulnerabilitiesTable(listOfBlocks, nazwa)

def openNessusFile(path):
    nazwa = str(path).split("\\")
    nazwa = nazwa[-1]
    nazwa = nazwa.split('.')[0]
    NessusVulnerabilities.main(path)



def getNmapPath(wildcard='*.*'):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()

    print path
    openNmapFile(path)
    #return path

def getNessusPath(wildcard='*.*'):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()

    print path
    openNessusFile(path)
    #return path

def getVulnerabilitiesTable(listOfBlocks, nazwa):
    listOfVulnerabilities = latexPDF.listOfServices(listOfBlocks)
    print listOfVulnerabilities
    makemydir(nazwa)
    os.chdir('..\\')
    makemydir(nazwa + "Podatnosci")
    os.chdir('..\\')
    latexPDF.createEmptyVulnerabilities(listOfVulnerabilities, sciezka=str(nazwa + "Podatnosci"))

def donothing():
   filewin = Tkinter.Toplevel()
   button = Tkinter.Button(filewin, text="Do nothing button")
   button.pack()


def createFolders():
    os.chdir(home+'\\Desktop')
    today = date.today()
    data = str(today).replace('-', '_')
    makemydir(nameFirm +'_'+ data)
    os.makedirs(nameRaport + '_SkanyNmap')
    os.makedirs(nameRaport + '_PodatnosciPDF')
    os.makedirs(nameRaport + '_PodatnosciTXT')
    os.makedirs(nameRaport + '_Tabele')


def createVulnerabilityTxt():
    path = os.getcwd()
    #obrazek = os.path.dirname(os.path.realpath(__file__))
    path = '\\'

def widget():
    root = Tkinter.Tk()
    menubar = Tkinter.Menu(root)
    filemenu = Tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Wybierz Datę Raportu", command=chooseDate)
    filemenu.add_command(label="Otwórz plik z Nmapa", command=getNmapPath)
    filemenu.add_command(label="Otwórz plik z Nessusa", command=getNessusPath)
    filemenu.add_command(label="Utwórz Puste Tabele Podatności", command=getVulnerabilitiesTable)
    filemenu.add_command(label="Utwórz Puste Tabele PodatnościTXT", command=createVulnerabilityTxt)
    filemenu.add_command(label="Zamknij", command=donothing)

    filemenu.add_separator()
    filemenu.add_command(label="Wyjście", command=root.quit)
    menubar.add_cascade(label="opcje", menu=filemenu)
    editmenu = Tkinter.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cofnij", command=donothing)

    editmenu.add_separator()

    editmenu.add_command(label="Wytnij", command=donothing)
    editmenu.add_command(label="Kopiuj", command=donothing)
    editmenu.add_command(label="Wklej", command=donothing)
    editmenu.add_command(label="Usuń", command=donothing)
    editmenu.add_command(label="Zaznacz wszsytko", command=donothing)

    menubar.add_cascade(label="Edytuj", menu=editmenu)
    helpmenu = Tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help", command=donothing)
    helpmenu.add_command(label="O Programie...", command=donothing)
    menubar.add_cascade(label="Pomoc", menu=helpmenu)

    root.config(menu=menubar)
    root.mainloop()


def chooseNmapFile():
    path = get_path('*.xml')
    return path


def main():
    #path = chooseNmapFile()
    widget()

if __name__ == "__main__":
    main()
