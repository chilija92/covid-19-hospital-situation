import requests
import json

res = requests.get("https://www.svt.se/special/articledata/2532/covid_region.json")
data = json.loads(res.content)
with open("..\Data\Sweden.csv", 'w', newline='') as myfile:
    myfile.write('date,hospital,icu,ventilator\n')
    for entry in data['sverige']['corona']:
        myfile.write(entry['Datum'] + ",," + str(entry['Covid19 (totalt)']) + ",\n")


