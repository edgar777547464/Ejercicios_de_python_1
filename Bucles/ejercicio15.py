

#//Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
#//euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
#//Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total 
#//de lo que pagó después de los 20 meses.

mes = 20

for i in range(1, 20 + 1):
    pago = int(input(f"Cuanto pagas en el mes:{i} "))
    total = pago ** mes
print(f"El tolat de la deuda es {total}")