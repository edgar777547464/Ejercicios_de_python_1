

#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados 
#por una distancia d. 
#El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo 
#para ingresar la distancia entre los dos vehículos (km) y sus respectivas 
#velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) 
#alcanzará el vehículo más rápido al otro.


v1 = float(input("Coloca la velocidad del coche 1: "))
v2 = float(input("Coloca la velocidad del cohe 2(va mas lento): "))
diatancia = int(input("A que distancia estan los coches: "))

tiempo = diatancia / (v1 - v2)
tiempo * 60

print("Lo alcanza en ",tiempo,"minutos")

