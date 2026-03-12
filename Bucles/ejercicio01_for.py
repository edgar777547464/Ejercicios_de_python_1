
# programa que calcula el factorial de un numero 

#5 factorial = 1*2*3*4*5

factorial = 1
n1 = int(input("Introduce un numero: "))

for i in range(1, n1 + 1):
	factorial= factorial * i 

print("El factorial de ",n1," es ",factorial)

