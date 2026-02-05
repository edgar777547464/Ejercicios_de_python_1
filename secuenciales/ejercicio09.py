

#Una tienda ofrece un descuento del 15% sobre el total de la compra y un 
#cliente desea saber cuanto deberá pagar finalmente por su compra.

precio_prenda = int(input("Precio de la prenda desada: "))

descuento = precio_prenda * 0.15
total_a_pagar = precio_prenda - descuento

print("precio con descuento del 15% es de ", total_a_pagar )