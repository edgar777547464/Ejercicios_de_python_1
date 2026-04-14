

#//Función ConvetirEspaciado: Recibe una cadena de caracteres, y devuelve otra 
#//con los mismos caracteres separados con espacio.
#//Parámetros de entrada: Cadena de caracteres
#//Dato devuelto: Cadena igual a la anterior pero con espacios entre los 
#//caracteres

def convertir_espaciado(cadena):
    resultado = ""
    for i in range(len(cadena)):
        resultado += cadena[i]
        if i < len(cadena) - 1:
            resultado += " "
    return resultado

mensaje = input("Introduce una cadena: ")
print("La cadena con espacio:", convertir_espaciado(mensaje))


    