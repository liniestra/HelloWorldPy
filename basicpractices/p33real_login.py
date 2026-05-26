usuario_input = input("Usuario: ")
password_input = input("Password: ")

login_correcto = False

with open("usuarios.txt", "r") as archivo:

    usuarios = archivo.readlines()

for usuario in usuarios:

    datos = usuario.strip().split(",")

    usuario_guardado = datos[0]
    password_guardado = datos[1]

    print(f"Usuario: {usuario_guardado}, Password: {password_guardado}")

    if usuario_input == usuario_guardado and password_input == password_guardado:
        login_correcto = True

if login_correcto:
    print("Acceso permitido")
else:
    print("Acceso denegado")