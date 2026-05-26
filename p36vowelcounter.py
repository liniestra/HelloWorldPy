texto = input("Inserta un texto para contar el número de vocales que tiene:\n").lower()
contador_vocales = 0

for letra in texto:
    if letra in "aeiou":
        contador_vocales += 1

contador_consonantes = 0
for letra in texto:
    if letra not in "aeiou":
        contador_consonantes += 1
print(f"El texto tiene {len(texto)} caracteres.")
print(f"El texto tiene {contador_vocales} vocales.")
print(f"El texto tiene {contador_consonantes} consonantes.")
