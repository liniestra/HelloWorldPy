print("A continuación verás un contador del 1 al 36 (de uno en uno), en la función range no cuenta hasta el último número que pongas en el segundo argumento, sino hasta uno antes.")
for numero in range(1,37):
    print(numero)
print("Ahora se supone que el siguiente contador es del 2 al 36 (de dos en dos)")
for numero in range(2,37,+2):
    print(numero)
print("Ahora se supone que el siguiente contador es del 36 al 2 (de dos en dos)")
for numero in range(37,2,-2):
    print(numero)