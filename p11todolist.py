def mostrar_tareas(tareas):
    print("Tus tareas pendientes son:")
    for t in tareas:
     print("* " + t)

tareas = []
while True:
    tarea = input("¿Qué tarea deseas agregar? Si deseas salir, escribe 'salir': ")
    if tarea == "salir":
        break
    tareas.append(tarea)

if not tareas:
    print("No tienes tareas pendientes.")
elif len(tareas) > 0 and len(tareas) < 4:
    print("Tienes pocas tareas pendientes.")
    mostrar_tareas(tareas)
elif len(tareas) >= 4 and len(tareas) <= 7:
    print("Tienes varias tareas pendientes.")
    mostrar_tareas(tareas)
elif len(tareas) > 7:
    print("Tienes muchas tareas pendientes. ¡Apúrale!")
    mostrar_tareas(tareas)