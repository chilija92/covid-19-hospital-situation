import csv, urllib.request
from datetime import datetime

countries = ["Albania", "Austria", "Belgium", "Denmark", "France", "Hungary", "Italy", "Ireland", "Netherlands",
             "Portugal", "Slovakia", "Slovenia", "Switzerland"]

countryList = {}
for country in countries:
    countryList[country] = []
    countryList[country].append(["date","hospital","icu","ventilator"])

url = 'https://raw.githubusercontent.com/ec-jrc/COVID-19/master/data-by-country/jrc-covid-19-all-days-by-country.csv'
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)
for line in cr:
    if line[2] in countries:
        countryList[line[2]].append([line[0],line[9], line[10], None])


for country, data in countryList.items():
    countryPath = "..\\Data\\" + country + ".csv"
    with open(countryPath, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        for entry in data:
            wr.writerow(entry)