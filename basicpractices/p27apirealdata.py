import requests

url = "https://restcountries.com/v3.1/name/mexico"

respuesta = requests.get(url)

datos = respuesta.json()

print("Nombre oficial del país:", datos[0]["name"]["official"])
print("País:", datos[0]["name"]["common"])
print("Capital:", datos[0]["capital"][0])
print("Población:", datos[0]["population"])
print("Timezones:", datos[0]["timezones"])