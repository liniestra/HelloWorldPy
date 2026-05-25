usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("Introduce tu nombre de usuario: \n")
contrasena = input("Introduce tu contraseña: \n")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Login exitoso")
else:
    print("Por favor revisa la información que ingresaste, el usuario o contraseña son incorrectos.")  