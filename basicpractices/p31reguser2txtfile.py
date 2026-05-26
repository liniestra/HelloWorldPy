usuario = input("Introduce tu nombre de usuario: \n")
contrasena = input("Introduce tu contraseña: \n")

with open("usuarios.txt", "a") as archivo:
    archivo.write("Usuario: " + usuario + "\n")
    archivo.write("Contraseña: " + contrasena + "\n")
