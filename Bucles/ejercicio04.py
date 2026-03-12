

cont_negativos = 0
cont_positivos = 0
cont_cero = 0

numero1 = int(input("¿Cuántos números vas a introducir?: "))

for i in range(numero1):
    print("Número", i + 1, ":")
    numero2 = int(input())

    if numero2 > 0:
        cont_positivos += 1
    elif numero2 < 0:
        cont_negativos += 1
    else:
        cont_cero += 1

print("Números positivos:", cont_positivos)
print("Números negativos:", cont_negativos)
print("Números igual a 0:", cont_cero)
