

#//Procedimiento CalcularMaxMin: recibe un vector de enteros, su tamaño, y devuelve
#// el máximo y el mínimo de los números guardados en el vector.
#//Parámetros de entrada: vector de enteros y tamaño
#//Parámetros de entrada y salida: valor máximo y mínimo

import random

def calcular_max_min(lista):
    vmax = lista[0]
    vmin = lista[0]
    for valor in lista[1:]:
        if valor > vmax:
            vmax = valor
        if valor < vmin:
            vmin = valor
    return vmax, vmin

lista = [random.randint(1, 100) for _ in range(10)]
vmax, vmin = calcular_max_min(lista)

print("Lista generada:", lista)
print("El valor máximo es", vmax)
print("El valor mínimo es", vmin)
