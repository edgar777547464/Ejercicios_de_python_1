
'''
cadenas de txto en python

'''

name = "Edgar"
lastName = "Corona"

print("I'am",name)

saludo = '"hello" es "hola"'

present_2 = 'I\'am',name  #poner "\" es para que tome la comilla como un comilla y no comoun cierre (baker lash)

menu = "Elige una opcion: \n opcion_1 \n opcion_2"

print(name)
print(lastName)
print(saludo)
print(present_2)
print(menu)

full_name = 'eDgar daVId COROna'
print(full_name.upper())  #todo lo pone en mayusculas
print(full_name.lower())  #todas las pone en minusculas
print(full_name.capitalize())  #solo la primera la pone en mayuscula
print(full_name.title())  # al inicio de cada palabra la pone en mayusculas
print(full_name.split(' '))  # separa la cadena de texto y te la da en lista

print("a" in "airpot")
print("hello" .endswith ("llo"))


