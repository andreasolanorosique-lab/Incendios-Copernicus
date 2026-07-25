import requests

url = (
    "https://services.arcgis.com/fFPraSowbm3gs7ek/"
    "arcgis/rest/services/EIregions_wActiveWildfires/"
    "FeatureServer?f=pjson"
)

r = requests.get(url, timeout=30)

print("Estado:", r.status_code)

datos = r.json()

print("\nCapas disponibles:\n")

for capa in datos["layers"]:
    print(capa["id"], "-", capa["name"])
