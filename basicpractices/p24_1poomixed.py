personas = []

class Persona:
    def __init__(self, nombre, edad, correo, telefono):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.telefono = telefono
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, mi correo es {self.correo} y mi teléfono es {self.telefono}.")

def crear_persona():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    correo = input("Ingrese el correo: ")
    telefono = input("Ingrese el teléfono: ")
    return Persona(nombre, edad, correo, telefono)

def mostrar_personas(personas):
    for persona in personas:
        persona.saludar()

print("Bienvenido al sistema de gestión de personas.")

while True:
    print("Seleccione una opción:")
    print("1. Crear persona")
    print("2. Mostrar personas")
    print("3. Eliminar persona")
    print("4. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        persona = crear_persona()
        personas.append(persona)
    elif opcion == "2":
        mostrar_personas(personas)
    elif opcion == "3":
        nombre_eliminar = input("Ingrese el nombre de la persona a eliminar: ")
        personas = [persona for persona in personas if persona.nombre != nombre_eliminar]
        mostrar_personas(personas)
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")