import urllib.request, csv
from datetime import datetime

url = "https://opendata.arcgis.com/datasets/c121a3cd3ca34e7b8050513307d41b93_0.csv"
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)
data = []
data.append(["data", "hospital", "icu", "ventilator"])
for i, row in enumerate(cr):
    if i > 0:
        time = datetime.strptime(row[0].split(' ')[0], '%Y/%m/%d').strftime('%Y-%m-%d')
        data.append((time, None, row[4], None))

with open("..\Data\\Netherlands.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    for entry in data:
        wr.writerow(entry)
