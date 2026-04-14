


#//Procedimiento CalcularAreaPerimetro: recibe el radio de una circunferencia y
#//devuelve el área y el perímetro.
#//Parámetros de entrada: radio (real)
#//Parámetros de entrada y salida: área y perímetro (real)

pi = 3.1416

radio = float(input("Introduce el radio: "))
area = pi * radio * radio
perimetro = 2 * pi * radio

print("Área:", area)
print("Perímetro:", perimetro)
