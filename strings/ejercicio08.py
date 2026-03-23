

palabra = input("Coloca una oración: ")

frase_nueva = ""
for letra in palabra:
    if letra.isupper():
        letra_nueva = letra.lower()
    else:
        letra_nueva = letra.upper()
    frase_nueva += letra_nueva  
    
print("Palabra original:", palabra)
print("Transformada:", frase_nueva)