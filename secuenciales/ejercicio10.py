

#Un alumno desea saber cual será su calificación final en la materia de 
#Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

calificacion1 = int(input("Coloca tu primer calificacion: "))
calificacion2 = int(input("Coloca tu segunda calificacion: "))
calificacion3 = int(input("Coloca tu tercera calificacion: "))

promedio_parciales = (calificacion1 + calificacion2 + calificacion3) /3

examen = float(input("Calificacion de tu examen: "))
trabajo_final = float(input("Calificacion de tu trabajo final: "))

calificacion_final = (promedio_parciales * 0.55) + (examen * 0.30) + (trabajo_final * 0.15)

print("Tu calificacion final es: ", calificacion_final)