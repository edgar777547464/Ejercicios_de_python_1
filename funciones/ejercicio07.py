

#//Función Login: Recibe un nombre de usuario y una contraseña, y devuelve un
#//Además va incrementa el numero de internos que la recibe como parámetro de 
#//entrada/salida
#//Parámetros de entrada: nombre y contraseña
#//Parámetros de entrada y salida: intentos
#//Dato devuelto: Valor lógico indicando si ha hecho login

intentos = 0
entrar = False

while not entrar and intentos < 3:
    usuario = input("Usuario: ")
    clave = input("Password: ")
    intentos += 1

    if usuario == "admin" and clave == "1234":
        entrar = True
    else:
        print("Error. Nombre de usuario o contraseña incorrecta.")

if entrar:
    print("Bienvenidos al sistema")
else:
    print("No has entrado en el sistema")
