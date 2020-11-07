import csv, urllib.request
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json

def init_czechia():
    url = 'https://opendata.ecdc.europa.eu/covid19/hospitalicuadmissionrates/csv/data.csv'
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    timeDict = {}
    for i, row in enumerate(cr):
        if i>0:
            if row[0] == "Czechia":
                if row[2] not in timeDict.keys():
                    timeDict[row[2]] = [row[2], None, None]
                if row[1] == "Daily hospital occupancy":
                    timeDict[row[2]][1] = row[4]
                elif row[1] == "Daily ICU occupancy":
                    timeDict[row[2]][2] = row[4]
    with open(".\Data\Czechia.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        wr.writerow(['date','hospitliziationsICU','invasiv'])
        for key, entry in timeDict.items():
            wr.writerow(entry)
    print(timeDict)

def getNewest():
    req = requests.get("https://onemocneni-aktualne.mzcr.cz/covid-19")
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('div',id="js-hospitalization-table-data")
    data = json.loads(table["data-table"])
    with open(".\Data\Czechia.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        wr.writerow(['date','hospital','icu','ventilator'])
        for entry in data["body"]:
            time = datetime.strptime(entry[0], '%d.%m.%Y').strftime('%Y-%m-%d')
            myfile.write(time+','+ str(entry[1]) + ',' + str(entry[2]) +",\n")

def getCzechia():
    getNewest()
    #init_czechia()