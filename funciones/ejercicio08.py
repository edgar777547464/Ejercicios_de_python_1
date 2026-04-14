

#//Función CalcularFactorial: Recibe un número si el número=1 devuelve que el 
#//factorial es 1, sino acumula el producto del número con el cálculo del factorial 
#//del numero-1. Es una función recursiva.
#//Parámetros de entrada: número
#////Dato devuelto: Factorial del número

numero = int(input("Número: "))
resultado = 1

for i in range(1, numero + 1):
    resultado = resultado * i

print("El factorial es:", resultado)
