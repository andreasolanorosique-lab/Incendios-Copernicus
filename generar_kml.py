import requests

url = (
    "https://services.arcgis.com/fFPraSowbm3gs7ek/"
    "arcgis/rest/services/EIregions_wActiveWildfires/"
    "FeatureServer/0?f=pjson"
)

r = requests.get(url, timeout=30)

print("Estado:", r.status_code)

datos = r.json()

print("Nombre de la capa:", datos["name"])
print("Tipo de geometría:", datos["geometryType"])
print("Máximo de registros:", datos["maxRecordCount"])
