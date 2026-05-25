import random
import string 

caracteres = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(12):
    password += random.choice(caracteres)
print("Contraseña generada:", password)