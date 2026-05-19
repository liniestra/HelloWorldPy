print("Esto es una calculadora sencilla, debes ingresar dos números para poderlos sumar, te los pediré uno a uno. Pueden ser números decimales o enteros, pero no dividas entre cero por favor.")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
if num2 != 0:
    division = num1 / num2
    print("La división es:", division)
else:
    print("Error: No se puede dividir entre cero.")
