from helper import helper
import csv

countries = ["Croatia", "Norway", "Latvia", "Lithuania", "Iceland"]

for country in countries:
    data = helper.filterCountry(country)
    path = "..\Data\\" + country + ".csv"
    with open(path, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        wr.writerow(["date", "hospital", "icu", "ventilator"])
        for date, entry in data.items():
            wr.writerow(entry)