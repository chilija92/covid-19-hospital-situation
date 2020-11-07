import csv
import urllib.request

def import_csv(csvfilename):
    data = []
    with open(csvfilename, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        for i, row in enumerate(reader):
            if row:  # avoid blank lines
                if i > 0:
                    data.append(row)
    return data

def filterCountry(country):
    url = 'https://opendata.ecdc.europa.eu/covid19/hospitalicuadmissionrates/csv/data.csv'
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    data = csv.reader(lines)
    countryData = {}
    for entry in data:
        if entry[0] == country:
            if entry[1] == 'Daily ICU occupancy':
                if entry[2] not in countryData.keys():
                    countryData[entry[2]] = [entry[2], None, entry[4], None]
                else:
                    countryData[entry[2]][2] = entry[4]
            elif entry[1] == 'Daily hospital occupancy':
                if entry[2] not in countryData.keys():
                    countryData[entry[2]] = [entry[2], entry[4], None, None]
                else:
                    countryData[entry[2]][1] = entry[4]
    return countryData