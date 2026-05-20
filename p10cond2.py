calificacion = input("¿Cuál es tu calificación?")
if calificacion == "10" or calificacion == "9":
    print("¡Excelente trabajo!")
elif calificacion == "8" or calificacion == "7":
    print("¡Buen trabajo! Pero puedes mejorar.")
elif calificacion == "6":
    print("¡Necesitas mejorar! Apenas pasaste.")
elif calificacion <= "5":
    print("Lo siento, has reprobado. Por favor estudia más.")