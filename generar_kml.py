import requests

url = "https://effis.jrc.ec.europa.eu/"

r = requests.get(url, timeout=30)

print("Código HTTP:", r.status_code)
print("Primeros 200 caracteres:")
print(r.text[:200])
