import json
from urllib.request import urlopen
from tabulate import tabulate

url = "https://ipinfo.io/json"
response = urlopen (url)
data = json.load(response)

print(data)

