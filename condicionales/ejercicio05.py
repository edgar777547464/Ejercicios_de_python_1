

#Escribe un programa que pida un nombre de usuario y una contraseña 
#y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
#sino se da un error.

usuario = input("Nombre de usuario: ")
contraseña = input("Contaseña: ")

if (usuario == "pepe") + (contraseña == "asdasd"):
	print("Inicio exitoso")

else:
	print("usuario y contraseña invalidos")
