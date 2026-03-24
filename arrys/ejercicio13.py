

#//De una empresa de transporte se quiere guardar el nombre de los conductores que 
#//tiene, y los kilómetros que conducen cada día de la semana.
#//Para guardar esta información se van a utilizar dos arreglos:
#// * Nombre: Vector para guardar los nombres de los conductores.
#// * kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
#//Se quiere generar un nuevo vector ("total_kms") con los kilómetros totales que 
#//realza cada conductor.
#//Al finalizar se muestra la lista con los nombres de conductores y los kilómetros 
#//que ha realizado.

tam_conductores_max = 10
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

num_conductores = 0
while True:
    num_conductores = int(input("¿Cuántos conductores tiene la empresa?: "))
    if num_conductores <= tam_conductores_max:
        break
    else:
        print(f"Como máximo puedo guardar la información de {tam_conductores_max} conductores")

nombres = ["" for _ in range(num_conductores)]
kms = [[0]*8 for _ in range(num_conductores)]

for indice_cond in range(num_conductores):
    nombres[indice_cond] = input(f"Nombre del conductor {indice_cond+1}: ")
    for indice_dias in range(7):
        kms[indice_cond][indice_dias] = int(input(f"¿Cuántos km ha realizado el {dias[indice_dias]}?: "))

for indice_cond in range(num_conductores):
    kms[indice_cond][7] = 0
    for indice_dias in range(7):
        kms[indice_cond][7] += kms[indice_cond][indice_dias]

for indice_cond in range(num_conductores):
    print(f"{nombres[indice_cond]} ha realizado {kms[indice_cond][7]} kms.")