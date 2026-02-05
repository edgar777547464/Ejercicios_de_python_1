

#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus 
#ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de 
#comisiones por las tres ventas que realiza en el mes y el total que 
#recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo_base = int(input("Cual es tu sueldo base: "))
print("")
venta_1 = int(input("Monto de la venta 1: "))
venta_2 = int(input("Monto de la venta 2: "))
venta_3 = int(input("Monto de la venta 3: "))

print("")

consepto1 = venta_1 * 0.10
consepto2 = venta_2 * 0.10
consepto3 = venta_3 *0.10

total = consepto1, consepto2, consepto3
pago_mes = sueldo_base , total

print("Total por concepto ",total )
print("Total, sueldo base + comisiones: ", pago_mes)