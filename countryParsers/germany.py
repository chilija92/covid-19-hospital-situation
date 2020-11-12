import csv, urllib.request
from datetime import datetime

def import_csv(csvfilename):
    data = []
    data.append(["date", "hospital", "icu", "ventilator"])
    with open(csvfilename, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        for row in reader:
            if row:  # avoid blank lines
                if row[0] != "date":
                    columns = [row[0], None, row[2], row[3]]
                    data.append(columns)
    return data

def getGermany():
    #archive
    data = import_csv(".\Data\Germany.csv")
    last_row = data[-1]

    #getNewest
    url = 'https://www.intensivregister.de/api/public/reporting/laendertabelle?format=csv'
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    gesamt = 0
    beatmet = 0
    time = None
    for i, row in enumerate(cr):
        if i>0:
            gesamt += int(row[5])
            beatmet += int(row[6])
        if i==1:
            time = row[4]


    #compare
    tAlt = datetime.strptime(last_row[0], '%Y-%m-%d')
    tNeu = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f%z')
    tNeu = datetime.strptime(tNeu.strftime('%Y-%m-%d'), '%Y-%m-%d')
    if tAlt.date() == tNeu.date():
        last_row[0] = tNeu.date()
        last_row[2] = gesamt
        last_row[3] = beatmet
    elif tAlt.date() < tNeu.date():
        data.append([tNeu.date(), None, gesamt, beatmet])

    with open(".\Data\Germany.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        for entry in data:
            wr.writerow(entry)


