#coding=utf-8
import pyPdf
import io

def readTextFromPDF(path):
    listLines = []
    pdf = pyPdf.PdfFileReader(open(path, "rb"))
    for page in pdf.pages:
        #print page.extractText()
        listLines.append(page.extractText())
    return listLines

def writePDFToText(path, listLines):

    name = str(path).split("\\")
    name = name[-1]
    name  = name.split('.')[0]
    name = path.split('.')[0]

    with open(name+str('TEKST.xml'), 'w') as file:
        for i in listLines:
            file.write(i.encode('utf8') + '\n')



def main(path):

    listLines = readTextFromPDF(path)
    print listLines
    writePDFToText(path, listLines)
if __name__ == "__main__":
    main()
