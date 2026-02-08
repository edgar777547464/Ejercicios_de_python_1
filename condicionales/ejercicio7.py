
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
#la base y el exponente. Pueden ocurrir tres cosas:
#El exponente sea positivo, sólo tienes que imprimir la potencia.
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base = int(input("Coloca  la base: "))
exponente = int(input("Coloca el exponente: "))

if exponente > 0:
	resultado = base** exponente
	print("El resultado es: ",resultado)

elif exponente == 0:
	print("El resultado es 1")

elif exponente < 0:
	resultado2 = 1/(base^abs(exponente))
	print("El resultado es: ",resultado2)
