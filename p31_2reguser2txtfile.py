import json

def registrar_usuario(usuario, contrasena):
    usuario_data = {
        "usuario": usuario,
        "contrasena": contrasena
    }

    with open("usuarios.json", "a") as archivo:
        json.dump(usuario_data, archivo)
        archivo.write("\n")

def editar_usuario(usuario, nueva_contrasena):
    usuarios = []

    with open("usuarios.json", "r") as archivo:
        for linea in archivo:
            usuario_data = json.loads(linea)
            if usuario_data["usuario"] == usuario:
                usuario_data["contrasena"] = nueva_contrasena
            usuarios.append(usuario_data)

    with open("usuarios.json", "w") as archivo:
        for usuario_data in usuarios:
            json.dump(usuario_data, archivo)
            archivo.write("\n")

def borrar_usuario(usuario):
    usuarios = []

    with open("usuarios.json", "r") as archivo:
        for linea in archivo:
            usuario_data = json.loads(linea)
            if usuario_data["usuario"] != usuario:
                usuarios.append(usuario_data)

    with open("usuarios.json", "w") as archivo:
        for usuario_data in usuarios:
            json.dump(usuario_data, archivo)
            archivo.write("\n")

def imprimir_usuarios():
    with open("usuarios.json", "r") as archivo:
        for linea in archivo:
            usuario_data = json.loads(linea)
            print(f"Usuario: {usuario_data['usuario']}, Contraseña: {usuario_data['contrasena']}")

print ("Bienvenido al sistema de registro de usuarios.")

while True:
    print("Qué quieres hacer?")
    print("1. Registrar usuario")
    print("2. Editar usuario")
    print("3. Borrar usuario")
    print("4. Imprimir usuarios")
    print("5. Salir")

    opcion = input("Introduce el número de la opción que deseas: \n")

    if opcion == "1":
        usuario = input("Introduce tu nombre de usuario: \n")
        contrasena = input("Introduce tu contraseña: \n")
        registrar_usuario(usuario, contrasena)
    elif opcion == "2":
        usuario = input("Introduce tu nombre de usuario: \n")
        nueva_contrasena = input("Introduce tu nueva contraseña: \n")
        editar_usuario(usuario, nueva_contrasena)
    elif opcion == "3":
        usuario = input("Introduce tu nombre de usuario: \n")
        borrar_usuario(usuario)
    elif opcion == "4":
        imprimir_usuarios()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break


usuario_data = {
    "usuario": usuario,
    "contrasena": contrasena
}

with open("usuarios.json", "a") as archivo:
    json.dump(usuario_data, archivo)
    archivo.write("\n")
