

#//Función Convertir_A_Segundos: Recibe una cantidad de horas, minutos y segundos 
#//y calcula a cuantos segundos corresponde.
#//Parámetros de entrada: hora, minutos y segundos
#//Dato devuelto: Segundos totales

def convertir_a_segundos(h, m, s):
    return h * 3600 + m * 60 + s

def convertir_a_hms(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    return h, m, s

opcion = 0
while opcion != 3:
    print("1.- Convertir a segundos")
    print("2.- Convertir a horas, minutos y segundos")
    print("3.- Salir")
    opcion = int(input("Opción: "))

    if opcion == 1:
        h = int(input("Horas: "))
        m = int(input("Minutos: "))
        s = int(input("Segundos: "))
        print("Corresponde a", convertir_a_segundos(h, m, s), "segundos.")
    elif opcion == 2:
        segund = int(input("Segundos: "))
        h, m, s = convertir_a_hms(segund)
        print("Corresponde a", h, ":", m, ":", s)
    elif opcion == 3:
        pass
    else:
        print("Opción incorrecta")
