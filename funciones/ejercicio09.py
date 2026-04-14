

#//Procedimiento Intercambiar: Recibe dos números como parámetros de entrada y 
#//salida e intercambia sus valores si el segundo es mayor que el primero.
#//Parámetros de entrada y salida: dos números

numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

while numero2 != 0:
    r = numero1 % numero2
    numero1 = numero2
    numero2 = r

print("MCD:", numero1)
