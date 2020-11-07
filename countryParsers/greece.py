import json, requests

req = requests.get("https://raw.githubusercontent.com/Covid-19-Response-Greece/covid19-data-greece/master/data/greece/NPHO/intensive_care_cases.json")
data = json.loads(req.content)
print(data["cases"])

with open("..\Data\Greece.csv", 'w', newline='') as myfile:
    myfile.write("date, hospital, icu, ventilator\n")
    for entry in data["cases"]:
        myfile.write(entry["date"] + ',,,' + str(entry["intensive_care"]) + "\n")