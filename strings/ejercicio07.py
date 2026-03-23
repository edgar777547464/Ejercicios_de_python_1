

frase = input("Coloca una frase: ")

while True:
    letra_1 = input("Ingresa una letra: ")
    if len(letra_1) == 1:
        break

while True:
    letra_2 = input("Ingresa una letra: ")
    if len(letra_2) == 1:
        break

while True:
    letra_3 = input("Ingresa una letra: ")
    if len(letra_3) == 1:
        break

frase_nueva = ""
for letra in frase:
    if letra == letra_1:   
        frase_nueva += letra_2
        
    else:
        frase_nueva += letra

print("La frase nueva es: \n" + frase_nueva)