

cadena = input("Escribe algo\n")
subcadena = input("Escribe una subcadena:\n")

if cadena.startswith(subcadena):
    print(cadena,"si comienza con",subcadena)

else:
    print(cadena,"no comienza con",subcadena)