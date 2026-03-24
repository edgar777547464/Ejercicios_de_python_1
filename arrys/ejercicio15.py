

#// Crear un programa de ordenador para gestionar los resultados de la quiniela de 
#//fútbol. Para ello vamos a utilizar dos tablas:
#// Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre 
#//de los equipos de cada partido. En la quiniela se indican 15 partidos.
#// Resultados: Es una tabla de enteros donde se indica el resultado. También tiene 
#//dos columnas, en la primera se guarda el número de goles del equipo que está 
#//guardado en la primera columna de la tabla anterior, y en la segunda los goles 
#//del otro equipo.
#//El programa ira pidiendo los nombres de los equipos de cada partido y el 
#//resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

num_equipos = 15
equipos = [["",""] for _ in range(num_equipos)]
resultados = [[0,0] for _ in range(num_equipos)]

for indice in range(num_equipos):
    equipos[indice][0] = input(f"Introduce el nombre del equipo 1 del partido {indice+1}: ")
    equipos[indice][1] = input(f"Introduce el nombre del equipo 2 del partido {indice+1}: ")
    resultados[indice][0] = int(input(f"Introduce los goles metidos por el equipo {equipos[indice][0]}: "))
    resultados[indice][1] = int(input(f"Introduce los goles metidos por el equipo {equipos[indice][1]}: "))

print("QUINIELA")
print("========")

for indice in range(num_equipos):
    if resultados[indice][0] > resultados[indice][1]:
        print(f"{equipos[indice][0]} - {equipos[indice][1]} -> 1")
    elif resultados[indice][0] < resultados[indice][1]:
        print(f"{equipos[indice][0]} - {equipos[indice][1]} -> 2")
    else:
        print(f"{equipos[indice][0]} - {equipos[indice][1]} -> X")