frutas = ["manzana", "pera", "sandía", "uva", "plátano", "naranja", "mango", "fresa"]
print(frutas)

print("Ahora te voy a pedir que elijas una fruta de la lista, elige desde el número 0 hasta el 7, si dices -1 también obtendrás la última fruta.")
opcion = int(input("¿Qué número de fruta deseas?"))
if opcion >= 0 and opcion < len(frutas):
    print("Has elegido la fruta: " + frutas[opcion])
elif opcion == -1:
    print("Has elegido la última fruta: " + frutas[-1])