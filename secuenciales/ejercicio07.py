

#Realiza un programa que reciba una cantidad de minutos
# y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = int(input("Coloca la cantidad de minutos que gustes: "))
horas = minutos // 60
resto = minutos % 60 
print(minutos,"minutos equivale a ",horas ," con ", resto )