import urllib.request, csv
from datetime import datetime

def getJapan():
    url = 'https://www.mhlw.go.jp/content/cases_total.csv'
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    timeDict = {}
    for i, row in enumerate(cr):
        if i>0:
            time = datetime.strptime(row[0], '%Y/%m/%d').strftime('%Y-%m-%d')
            timeDict[row[0]] = [time, row[1], None, None]

    url = "https://www.mhlw.go.jp/content/severe_daily.csv"
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    for i, row in enumerate(cr):
        if i>0:
            timeDict[row[0]][2] = row[1]


    with open(".\Data\Japan.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        wr.writerow(['date','hospital','icu', 'ventilator'])
        for key, entry in timeDict.items():
            wr.writerow(entry)