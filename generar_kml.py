import requests

url = "https://maps.effis.emergency.copernicus.eu/effis"

r = requests.get(url, timeout=30)

print("Estado:", r.status_code)
print(r.text[:500])
