import urllib.request, csv

def getMexico():
    url = 'https://raw.githubusercontent.com/mexicovid19/Mexico-datos/master/datos_abiertos/series_de_tiempo/nuevos/covid19_' \
          'mex_hospitalizados.csv'
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    timeDict = {}
    for i, row in enumerate(cr):
        if i>0:
            timeDict[row[0]] = [row[0], row[1], None, None]

    url = "https://raw.githubusercontent.com/mexicovid19/Mexico-datos/master/datos_abiertos/series_de_tiempo/nuevos/" \
          "covid19_mex_uci.csv"
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    for i, row in enumerate(cr):
        if i>0:
            timeDict[row[0]][2] = row[1]


    with open(".\Data\Mexico.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        wr.writerow(['date','hospital','icu', 'ventilator'])
        for key, entry in timeDict.items():
            wr.writerow(entry)
