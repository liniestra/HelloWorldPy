import json

with open("persona.json", "r") as archivo:
    persona = json.load(archivo)

print("Contenido del archivo persona.json:")
print(json.dumps(persona, indent=4))
