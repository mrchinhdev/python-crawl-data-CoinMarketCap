from urllib.parse import urlencode
import requests
from tabulate import tabulate
import csv
import locale

with open('data.csv', 'a',newline='') as f:
    lsttieude = ['Name','Volume']
    writer = csv.writer(f)
    writer.writerow(lsttieude)
query_string = [
    ('start', '1'),
    ('limit', '8353'),
    ('sortBy', 'market_cap'),
    ('sortType', 'desc'),
    ('convert', 'USD'),
    ('cryptoType', 'all'),
    ('tagType', 'all'),
]

base = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?"
response = requests.get(f"{base}{urlencode(query_string)}").json()

results = [
    [
        currency["name"],
        round(currency["quotes"][0]["volume24h"], 4),
    ]
    for currency in response["data"]["cryptoCurrencyList"]
]

#print(tabulate(results, headers=["Currency", "Volume24H"], tablefmt="pretty"))

for i in results:
        b = '{:20,.4f}'.format(i[1])
        with open('data.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([i[0],'$'+b])
