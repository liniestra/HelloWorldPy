with open("usuarios.txt", "r") as archivo:

    usuarios = archivo.readlines()

for usuario in usuarios:
    print(usuario.strip())