import urllib.request, csv
from datetime import datetime

url = 'https://api.covidtracking.com/v1/us/daily.csv'
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)
data = []
data.append(["data", "hospital", "icu", "ventilator"])
for i, row in enumerate(cr):
    if i > 0:
        time = datetime.strptime(row[0], '%Y%m%d').strftime('%Y-%m-%d')
        data.append((time, row[5], row[7], row[9]))

with open("..\Data\\USA.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    for entry in data:
        wr.writerow(entry)