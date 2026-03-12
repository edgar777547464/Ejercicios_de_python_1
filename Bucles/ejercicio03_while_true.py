
suma = 0
cont = 0
numero1 = int(input("coloca tu primer numero: "))

while True: 
	suma = suma + numero1
	cont = cont +1
	print("Numero(0 para salir)")
	num = int(input())

	if numero1 != 0:
		cont = cont +1

	if numero1 == 0:
		break

if(cont != 0):
	media= suma / cont

else:
	media = 0

	print("La suma es: ",suma)
	print("La media es: ",media)
	