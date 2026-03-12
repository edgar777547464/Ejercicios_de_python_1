
suma = 0
cont = 0
numero1 = int(input("coloca tu primer numero: "))

while numero1 != 0:
	suma = suma + numero1
	cont = cont +1
	print("Numero(0 para salir)")
	num = int(input())

if cont > 0:
	media = suma / cont
else:
	media = 0

print("El resultado es ",suma)
print("L a media es: ",media)
