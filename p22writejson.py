import json

persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

with open("persona.json", "w") as archivo:
    json.dump(persona, archivo, indent=4)

print("El diccionario ha sido guardado en persona.json")
