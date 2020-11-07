import requests
import csv
from datetime import datetime

def getPoland():
    response = requests.get("https://docs.google.com/spreadsheets/d/1ierEhD6gcq51HAm433knjnVwey4ZE5DCnu1bW7PRG3E/export?format=csv&id=1ierEhD6gcq51HAm433knjnVwey4ZE5DCnu1bW7PRG3E&gid=1136959919", {
      "headers": {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "de-DE,de;q=0.9,en-DE;q=0.8,en;q=0.7,hr-HR;q=0.6,hr;q=0.5,en-US;q=0.4,bs;q=0.3",
        "sec-fetch-dest": "iframe",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "upgrade-insecure-requests": "1",
        "x-chrome-connected": "source=Chrome,id=104841564629346484380,mode=0,enable_account_consistency=false,consistency_enabled_by_default=false",
        "x-client-data": "CJW2yQEIorbJAQjBtskBCKmdygEIl6zKAQjKuMoBCKvHygEI9cfKAQjpyMoBCLTLygEIis/KAQjc1coBCIiZywEIl5rLARiKwcoB"
      },
      "referrer": "https://docs.google.com/spreadsheets/d/1ierEhD6gcq51HAm433knjnVwey4ZE5DCnu1bW7PRG3E/edit",
      "referrerPolicy": "strict-origin-when-cross-origin",
      "method": "GET",
      "mode": "cors",
      "credentials": "include"
    })


    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')

    lines = response.content.decode().split("\n")
    data = []
    data.append(["data", "hospital", "icu", "ventilator"])
    for i,line in enumerate(lines):
        if i > 4:
            lineNew = line.split(',')
            time = datetime.strptime(lineNew[0], '%d.%m').strftime('2020-%m-%d')
            if len(lineNew[6]) > 0:
                data.append([time, lineNew[1], None, lineNew[8]])
            else:
                data.append([time, lineNew[1], None, lineNew[7]])

    with open(".\Data\Poland.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        for entry in data:
            wr.writerow(entry)
