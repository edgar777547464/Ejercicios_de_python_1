

#// Crear un programa que lea los precios de 5 artículos y las cantidades vendidas 
#//por una empresa en sus 4 sucursales. Informar:
#// * Las cantidades totales de cada articulo.
#// * La cantidad de artículos en la sucursal 2.
#// * La cantidad del articulo 3 en la sucursal 1.
#// * La recaudación total de cada sucursal.
#// * La recaudación total de la empresa.
#// * La sucursal de mayor recaudación.

precio = []
for indice_art in range(5):
    valor = float(input(f"Ingrese Precio Articulo {indice_art+1}: "))
    precio.append(valor)

cantidad = [[0]*5 for _ in range(4)]
for indice_sucursal in range(4):
    for indice_art in range(5):
        cantidad[indice_sucursal][indice_art] = float(input(f"Ingrese Cant. de Articulo {indice_art+1}, en Sucursal {indice_sucursal+1}: "))

print("Cantidades por artículos:")
for indice_art in range(5):
    suma = cantidad[0][indice_art] + cantidad[1][indice_art] + cantidad[2][indice_art] + cantidad[3][indice_art]
    print(f"Total articulo {indice_art+1}: {suma}")

articulos_sucursal2 = 0
for indice_art in range(5):
    articulos_sucursal2 += cantidad[1][indice_art]
print(f"Total Sucursal 2: {articulos_sucursal2}")

print(f"Sucursal 1, Articulo 3: {cantidad[0][2]}")

mayor_rec = 0
num_mayor = 0
total_empresa = 0

for indice_sucursal in range(4):
    total_sucursal = 0
    for indice_art in range(5):
        total_sucursal += cantidad[indice_sucursal][indice_art] * precio[indice_art]
    print(f"Recaudaciones Sucursal {indice_sucursal+1}: {total_sucursal}")
    if total_sucursal > mayor_rec:
        mayor_rec = total_sucursal
        num_mayor = indice_sucursal+1
    total_empresa += total_sucursal

print(f"Recaudación total de la empresa: {total_empresa}")
print(f"Sucursal de Mayor Recaudación: {num_mayor}")