import urllib.request, csv

url = "https://raw.githubusercontent.com/M3IT/COVID-19_Data/master/Data/COVID_AU_national.csv"
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)
data = []
data.append(["data", "hospital", "icu", "ventilator"])
for i, row in enumerate(cr):
    if i > 0:
        data.append((row[0], row[12], row[14], row[16]))

with open("..\Data\\Australia.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    for entry in data:
        wr.writerow(entry)