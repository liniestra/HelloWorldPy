edad = int(input("¿Cuál es tu edad? "))
if edad >= 18 and edad < 50:
    print("Eres mayor de edad! Ya puedes entrar al bar")
elif edad == 50:
    print("Eres un adulto, solo sé responsable con tu consumo")
elif edad < 18:
    print("Eres menor de edad! No puedes entrar al bar. Regresa cuando seas mayor de edad!")