from urllib.parse import urlencode
from json import dumps
from requests import get


def getUK():
    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
    AREA_TYPE = "overview"

    filters = [
        f"areaType={ AREA_TYPE }",
    ]
    structure = {
        "date": "date",
        "hospital": "hospitalCases",
        "icu": None,
        "ventilator": "covidOccupiedMVBeds"
    }
    api_params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":")),
        "format": "csv"
    }
    response = get(ENDPOINT, params=api_params, timeout=10)
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
    with open(".\Data\\UK.csv", 'w', newline='') as myfile:
        myfile.write(response.content.decode())
