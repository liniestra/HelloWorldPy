alumnos = []

for i in range(3):

    nombre = input("Nombre: ")
    promedio = float(input("Promedio: "))

    alumno = {
        "nombre": nombre,
        "promedio": promedio
    }

    alumnos.append(alumno)

print("\nALUMNOS")

for alumno in alumnos:

    print(alumno["nombre"], "-", alumno["promedio"])