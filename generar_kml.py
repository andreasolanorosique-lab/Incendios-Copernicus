import requests

url = (
    "https://services.arcgis.com/fFPraSowbm3gs7ek/"
    "arcgis/rest/services?f=pjson"
)

r = requests.get(url, timeout=30)

print("Estado:", r.status_code)

datos = r.json()

print("\nServicios encontrados:\n")

for servicio in datos.get("services", []):
    print("-", servicio["name"], "(", servicio["type"], ")")
