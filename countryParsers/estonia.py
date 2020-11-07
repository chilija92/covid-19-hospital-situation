from datetime import datetime
import urllib.request, csv

def getEstonia():
    url = 'https://opendata.digilugu.ee/opendata_covid19_hospitalization_timeline.csv'
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    data = []
    for i, row in enumerate(cr):
        if i > 0:
            time = datetime.strptime(row[1], '%Y-%m-%dT%H:%M:%S%z').strftime('%Y-%m-%d')
            data.append([time, row[3],row[6], row[5]])

    with open(".\Data\Estonia.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        wr.writerow(["date","hospital","icu", "ventilator"])
        for entry in data:
            wr.writerow(entry)