import requests
import json, csv

url = 'https://raw.githubusercontent.com/COVID-19-Bulgaria/covid-database/master/Bulgaria/DateDiffCasesDataset.json'
response = requests.get(url)
data = json.loads(response.content)
bulgariaData = []
lastHospital = 0
lastICU = 0
bulgariaData.append(["data", "hospital", "icu", "ventilator"])
for key, value in data['hospitalized'].items():
    if value["cases"] == None and data['intensive_care'][key]['cases'] == None:
        pass
    else:
        lastHospital += value["cases"]
        lastICU += data['intensive_care'][key]['cases']
        bulgariaData.append([key, lastHospital, lastICU, None])

with open("..\Data\Bulgaria.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    for entry in bulgariaData:
        wr.writerow(entry)