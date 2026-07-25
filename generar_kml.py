import requests
import json

url = (
    "https://services.arcgis.com/fFPraSowbm3gs7ek/"
    "arcgis/rest/services/EIregions_wActiveWildfires/"
    "FeatureServer/0/query"
)

params = {
    "where": "1=1",
    "outFields": "*",
    "returnGeometry": "true",
    "f": "geojson"
}

r = requests.get(url, params=params, timeout=60)

print("Estado:", r.status_code)

datos = r.json()

print("Tipo:", datos["type"])
print("Número de incendios:", len(datos["features"]))

if datos["features"]:
    primero = datos["features"][0]

    print("Geometría:", primero["geometry"]["type"])
    print("Campos disponibles:")
    print(list(primero["properties"].keys()))
