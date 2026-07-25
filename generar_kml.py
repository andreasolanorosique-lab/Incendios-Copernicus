import requests

url = "https://maps.effis.emergency.copernicus.eu/effis"

r = requests.get(url, timeout=30)

print("URL final:", r.url)
print("Estado:", r.status_code)
print("Tipo:", r.headers.get("content-type"))
