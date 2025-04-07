import random
import string
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud_contraseña = int(input("Cuantos caracteres quieres que tenga tu contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation  # Letras, dígitos y símbolos

# Crear una variable vacía donde se almacenará la contraseña generada
contraseña_generada = ""

# Usar un bucle para generar la contraseña
for _ in range(longitud_contraseña):
    # Elegir un carácter aleatorio de la variable 'caracteres' y añadirlo a la contraseña
    contraseña_generada += random.choice(caracteres)

# Mostrar la contraseña generada
print("Tu contraseña generada es:", contraseña_generada)
