# -*- coding: utf-8 -*-
import main2

from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image

import PyPDF2
import os
import subprocess
import StringIO

listOfBlocks, data, godzina, hostUp, liczbaHostowWSieci = main2.main()


def listOfServices(listBlocks):
    listServices = []
    for i in listBlocks:
        for j in i.portsList:
            if j[3] != 'unknown,':
                o=str(j[3]).replace(',', '')
                o2= o.replace('?', '')
                listServices.append(o2)

    listServices =  list(set(listServices))
    return listServices

def returnData(listOfBlocks):
    data = []
    data.append(['Adres IP Hosta', 'Otwarte i Filtrowane Porty', 'Nazwa Usługi', 'Uwagi'])
    stareIP = 0

    for i in listOfBlocks:
        #print i.ip, i.portsList
        for j in i.portsList:
            #print j[0], j[1], j[2], j[3]

            if i.ip != stareIP:
                if '?' in str(j[3]):
                    data.append([str(i.ip).replace(',', ''), str(j[0]) + '/' + str(j[1]) + ' ' + str(j[2]), str(j[3]).replace('?,', ''), 'Wskazania nie są pewne'])
                else:
                    data.append([str(i.ip).replace(',','') ,str(j[0]) +'/'+ str(j[1]) + ' ' + str(j[2]), j[3], ' '])
                stareIP = i.ip

            else:
                if '?' in str(j[3]):
                    data.append([' ', str(j[0]) + '/' + str(j[1]) + ' ' + str(j[2]), str(j[3]).replace('?,', ''),
                                 'Wskazania nie są pewne'])
                else:
                    data.append([' ',str(j[0]) +'/'+ str(j[1]) + ' ' + str(j[2]), str(j[3]).replace(',', ''), ' '])

    return data

def createTable(data, nazwa, nameRaport):

    komorka = 0
    listaKomorek = []
    for i in data: #dane z return data
        if str(i[0]) != ' ':
            listaKomorek.append(komorka)
        komorka += 1


    doc = SimpleDocTemplate(nazwa+ ".pdf", pagesize=letter)
    elements = []
    blueEnergy = colors.Color(red=(38.0/255), green=(53.0/255), blue=(139.0/255))

    t = Table(data)
    width, height = A4
    # dodanie czcionek
    pdfmetrics.registerFont(TTFont('Century Gothic','GOTHIC.TTF'))

    t.setStyle(TableStyle([ ('BACKGROUND', (0,0), (3,0) , blueEnergy),
                            ('GRID', (0, 0), (3, 0), 0.35, colors.white),
                            ('FONT', (0, 0), (3, 0), 'Century Gothic', 11),
                            ('TEXTCOLOR', (0, 0), (3, 0), colors.white),
                            ('FONT', (1, 1), (-1, -1), 'Century Gothic', 9),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('SPAN', (0, -1), (-2, -1)),
                           ('GRID', (1, 1), (3, -2), 0.35, colors.black),
                            ('BOX', (0, 1), (3, -2), 0.35, colors.black),
                            ('BOX', (0, 0), (3, 0), 0.35, colors.black),
                           ]))

    for i in listaKomorek:
        t.setStyle(TableStyle([('LINEABOVE', (0, i), (3, i), 0.35, colors.black)]))

    elements.append(t)
    doc.build(elements)

def createEmptyVulnerabilities(listOfVulnerabilities, sciezka):
    for i in listOfVulnerabilities:
        createTableVulnerabilities(nazwa = str(i), nazwaPliku="podatnosc_"+str(i), sciezka=sciezka)

def createTableVulnerabilities(nazwa = "NazwaZagrozenia", id="ID", poziom=0, opisZagrozenia = 'opis', skutek = 'skutek', nazwaPliku='_', opisTechniczny='Techniczny', rekomendacja='rekomendacja', sciezka=''):

    if float(poziom) >= 9.0:
        obrazek = Image('Image/czerwony.jpg')
    if float(poziom) >= 5.0 and float(poziom) < 9.0:
        obrazek = Image('Image/pomaranczowy.jpg')
    if float(poziom) >= 3.0:
        obrazek = Image('Image/zolty.jpg')
    if float(poziom) < 3.0:
        obrazek = Image('Image/zolty.jpg')

    data = []
    data.append(['Nazwa\nZagrożenia', nazwa, 'ID\nzagrożenia',id, 'Poziom\nKrytyczności\n[CVSS]', poziom, obrazek])
    data.append(['Opis Zagrożenia', opisZagrozenia])
    data.append(['Skutek\nMaterializacji\nZagrożenia', skutek])
    data.append(['Opis Techniczny', opisTechniczny])
    data.append(['Rekomendacja', rekomendacja])
    # container for the 'Flowable' objects
    elements = []
    blueEnergy = colors.Color(red=(38.0 / 255), green=(53.0 / 255), blue=(139.0 / 255))
    blueEnergyBackground = colors.Color(red=(242.0 / 255), green=(242.0 / 255), blue=(242.0 / 255))
    t = Table(data)
    width, height = A4
    # dodanie czcionek
    pdfmetrics.registerFont(TTFont('Century Gothic','GOTHIC.TTF'))
    pdfmetrics.registerFont(TTFont('Century Gothic Bold', 'GOTHIC.TTF'))

    t.setStyle(TableStyle([
                            ('FONT', (0, 0), (-1, -1), 'Century Gothic', 11),
                            ('FONT',  (1, 0), (1, 0), 'Century Gothic Bold', 11),
                            ('TEXTCOLOR', (1, 0), (1, 0), blueEnergy),
                            ('BACKGROUND', (0, 0), (0, 3), blueEnergyBackground),
                            ('BACKGROUND', (2, 0), (2, 0), blueEnergyBackground),
                            ('BACKGROUND', (0, 4), (0, 4), blueEnergyBackground),

                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('SPAN', (1, 1), (6, 1)),
                            ('SPAN', (1, 2), (6, 2)),
                            ('SPAN', (3, 1), (6, 1)),
                            ('SPAN', (1, 3), (6, 3)),
                            ('SPAN', (1, 4), (6, 4)),
                            ('GRID', (0, 0), (-1, -1), 0.35, colors.black),
                           ]))

    elements.append(t)
    try:
        doc = SimpleDocTemplate( name+ '_PodatnosciPDF\\' + nazwaPliku + ".pdf", pagesize=letter)
    except:
        doc = SimpleDocTemplate(nazwaPliku + ".pdf", pagesize=letter)

    doc.build(elements)

def main():
    data = returnData()
    createTable(data)
    createTableVulnerabilities()
    createTableVulnerabilities('Zagrozenie A', 'A1',4.9, 'Bardzo steraszne zagrozenie\nAAAAAAAAAAAAAAAA', 'Qniec Świata')


if __name__ == "__main__":
    main()