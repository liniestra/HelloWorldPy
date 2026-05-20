contactos = {}
while True:
    nombre = input("Dame el nombre de tu nuevo contacto (o salir para terminar)")

    if nombre == "salir":
        break

    telefono = input("Dame el teléfono de tu nuevo contacto: ")
    contactos[nombre] = telefono

print("Tu agenda de contactos:")
for nombre, telefono in contactos.items():
    print("Nombre:", nombre, ", Teléfono:", telefono)