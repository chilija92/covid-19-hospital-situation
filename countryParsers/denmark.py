from helper import helper
import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def initDenmark():
    data = helper.import_csv(".\Data\Denmark.csv")
    #data = helper.filterCountry("Denmark")
    return data


def getNewest():
    req = requests.get("https://www.sst.dk/da/corona/tal-og-overvaagning")
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.findAll('table')
    patientenRows = table[6].findAll("tr")
    intensivRows = table[7].findAll("tr")
    ventilatorRows= table[8].findAll("tr")
    dataDict = {}
    for i, row in enumerate(patientenRows):
        if i > 0:
            cells = row.findAll("td")
            time = datetime.strptime(cells[0].get_text().strip(), '%d/%m').strftime('2020-%m-%d')
            dataDict[time] = [time, cells[1].get_text().strip(), intensivRows[i].findAll("td")[1].get_text().strip(),
                              ventilatorRows[i].findAll("td")[1].get_text().strip()]
    return dataDict

def getDenmark():
    data = initDenmark()
    dataNew = getNewest()
    with open(".\Data\Denmark.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        wr.writerow(["date", "hospital", "icu", "ventilator"])
        for date, entry in data.items():
            if date not in dataNew.keys():
                wr.writerow(entry)
        for date, entry in dataNew.items():
            wr.writerow(entry)

