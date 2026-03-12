

cadena = input("Coloca una frase: ")
caracter = input("Coloca una letra: ")

repetidas = 0
for i in cadena:
    if i == caracter:
        repetidas += 1

print(f"la letra es {caracter} se encuentra {repetidas} veces dentro de la palabra {cadena}")