import requests

url = "https://maps.effis.emergency.copernicus.eu/geoserver/wfs?service=WFS&request=GetCapabilities"

r = requests.get(url, timeout=60)

print("Estado:", r.status_code)
print("Tipo:", r.headers.get("content-type"))
print(r.text[:500])
