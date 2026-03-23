

frase = input("Coloca una frase: ")

word = input("Coloca una palabra: ")

if word in frase:
    print(frase.replace(word, f'"{ word}"'))
else:
    print("La palabra no se encuentra en la frase")