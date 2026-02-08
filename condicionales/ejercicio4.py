

#Crea un programa que pida al usuario dos números y muestre su división 
#si el segundo no es cero, o un mensaje de aviso en caso contrario.

n1 = int(input("Coloca tu primer numero: "))
n2 = int(input("coloca tu segundo numero: "))

if n2 ==0:
	print("No se puede dividir entre 0")

else:
	r = n1 / n2
	print("La divicion es ",r)