import urllib.request, csv

url = "https://health-infobase.canada.ca/src/data/covidLive/covid19-epiSummary-hospVentICU.csv"
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)
data = []
data.append(["data", "hospital", "icu", "ventilator"])
for i, row in enumerate(cr):
    if i > 0:
        data.append((row[0], row[8], row[6], row[9]))

with open("..\Data\\Canada.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    for entry in data:
        wr.writerow(entry)