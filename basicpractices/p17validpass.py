password = input("Introduce una contraseña válida: ")

if len(password) < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
elif not any(char.isdigit() for char in password):
    print("La contraseña debe contener al menos un número.")
elif not any(char.isupper() for char in password):
    print("La contraseña debe contener al menos una letra mayúscula.")
elif not any(char.islower() for char in password):
    print("La contraseña debe contener al menos una letra minúscula.")
else:
    print("Contraseña válida.")