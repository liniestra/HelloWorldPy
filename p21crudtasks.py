tareas = []
while True:
    try:
        print("\n1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = int(input("Selecciona una opción: "))
        if opcion == 1:
            tarea = input("Introduce la tarea que deseas agregar: ")
            tareas.append(tarea)
            print("Tarea agregada.")
        elif opcion == 2:
            if tareas:
                print("Lista de tareas:")
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")
            else:
                print("No hay tareas en la lista.")
        elif opcion == 3:
            if tareas:
                print("Lista de tareas:")
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")
                indice = int(input("Introduce el número de la tarea que deseas eliminar: "))
                if 1 <= indice <= len(tareas):
                    tareas.pop(indice - 1)
                    print("Tarea eliminada.")
                else:
                    print("Índice inválido.")
            else:
                print("No hay tareas en la lista.")
        elif opcion == 4:
            print("\nSaliendo del programa.")
            break
        else:
            print("\nOpción inválida. Por favor, selecciona una opción válida.")
    except:
        print("\nError: Por favor, introduce un número válido para seleccionar una opción.")