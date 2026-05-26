import random

numero_secreto = random.randint(1, 10)

while True:
    intento = int(input("Adivina el número secreto (entre 1 y 10): "))
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! Adivinaste el número secreto.")
        break