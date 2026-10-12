import csv
import requests

URL = "https://api.nbp.pl/api/exchangerates/tables/C?format=json"

response = requests.get(URL)
response.raise_for_status()
data = response.json()

rates = data[0]["rates"]

with open("kursy_walut.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")

    writer.writerow(["currency", "code", "bid", "ask"])

    for rate in rates:
        writer.writerow(
            [rate["currency"], rate["code"], rate["bid"], rate["ask"]]
        )