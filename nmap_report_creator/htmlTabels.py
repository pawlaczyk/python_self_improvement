#coding=utf-8
import main2
import HTMLParser
import string

listOfBlocks, data, godzina, hostUp, liczbaHostowWSieci = main2.main()

def createScheme(nazwaRaportu, nazwaTabeli = "Tabela"):
    """Funkcja Tworząca szablon raportu tabeli"""

    my_div_data = "some_data_to_display_in_HTML"
    TEMPLATE_FORMAT = """
    <html>
    <head> <title>Raport Tabela </title></head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <link rel="stylesheet" href="CSSTable.css" type="text/css">
    <body>
        <div class = "myclass">"""+ nazwaTabeli +"""</div>
        <table class=CSSTable width=90%>
    """

    TEMPLATE = string.Template(TEMPLATE_FORMAT)
    html_data = TEMPLATE.safe_substitute()

    open(nazwaRaportu, "w").write(html_data)
    createTable(nazwaRaportu,listOfBlocks)

    TEMPLATE_FORMAT = """
    </table>
    </body>
    </html>
    """

    TEMPLATE = string.Template(TEMPLATE_FORMAT)
    html_data = TEMPLATE.safe_substitute()

    open(nazwaRaportu, "a").write(html_data)


def createTable(nazwaRaportu, listOfBlocks):
    stareIP = "0"

    for i in listOfBlocks:
        porty = []
        ip = i.ip
        for j in str(i.portsList).split('), ('):
            try:
                j = j.replace("[('", "")
                j = j.replace(")]", "")
                j = j.replace("', '", " ")
                j = j.replace("'", "")
                j = j.replace(",", "")

                porty.append(j.split(' ')[0]) #nr portu
                porty.append(j.split(' ')[1]) #czy tcp
                porty.append(j.split(' ')[3]) #nazwa uslugi

                if i.ip != stareIP:
                    createRow(nazwaRaportu,ip, porty[0], porty[1], porty[2])
                else:
                    createRow(nazwaRaportu, '', porty[0], porty[1], porty[2])
                stareIP = i.ip

            except:
                pass


def createRow(nazwaRaportu, ip, port,czyTcp,  nazwa_uslugi):
    """Funkcja tworząca wiersz w kolumnie"""
    TABLE_FORMAT = """
    <tr>
        <td>""" + str(ip).replace(',', '') +"""</td>
        <td>""" + port +'/'+czyTcp +"""</td>
        <td>""" + str(nazwa_uslugi).replace('?', '') +"""</td>
    </tr>
    """


    TEMPLATE = string.Template(TABLE_FORMAT)
    html_data = TEMPLATE.safe_substitute()

    open(nazwaRaportu, "a").write(html_data)


def main():
    #createScheme('raport.html')
    pass


if __name__ == "__main__":
    main()