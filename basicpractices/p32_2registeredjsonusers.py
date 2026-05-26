import json

with open("usuarios.json", "r") as archivo:

    for linea in archivo:
        usuario_data = json.loads(linea)
        print(f"Usuario: {usuario_data['usuario']}, Contraseña: {usuario_data['contrasena']}")
