import requests, csv
from bs4 import BeautifulSoup
from datetime import datetime

req = requests.get("https://covid19.public.lu/fr/graph.html")
soup = BeautifulSoup(req.content, 'html.parser')
rows = soup.findAll('div',class_="chart-lines")[4].find("tbody").findAll("tr")
data = []
data.append(["date", "hospital", "icu", "ventilator"])
for row in rows[1:]:
    cells = row.find_all("td")
    time = datetime.strptime(cells[0].get_text(), '%d/%m/%Y').strftime('%Y-%m-%d')
    data.append([time, cells[2].get_text(), cells[1].get_text(), None])

with open("..\Data\Luxembourg.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    for entry in data:
        wr.writerow(entry)