import requests
import json, csv
from datetime import datetime

url = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaHospitalData'
response = requests.get(url)
data = json.loads(response.content)
finlandData = []
finlandData.append(["data", "hospital", "icu", "ventilator"])
for entry in data['hospitalised']:
    if entry["area"] == "Finland":
        date = datetime.strptime(entry["date"], '%Y-%m-%dT%H:%M:%S.%f%z').date()
        datum = date.strftime('%Y-%m-%d')
        finlandData.append([datum, entry['totalHospitalised'], entry['inIcu'], None])

with open("..\Data\Finland.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    for hospData in finlandData:
        wr.writerow(hospData)