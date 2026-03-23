
'''
Funciones en python

print("Un texto o mensaje")  ---> imprimir en terminal
int("5") ---> regresa un valor entero
input("Texto")  ---> regresa texto 
len(Objeto)  ---> regresa el tamaño del objeto
range(5) ---> regresa una coleccionde valores 

'''
'''
podemos crear funciones 
Definir la funcion

def nombre_de_funcion(parametros):
    instruciones
    retun algo


llamar o ejecutar
nombre_funcion()
'''
#sin parametro y sin retorno
def hello():
    print(hello)

hello()
hello()
hello()
hello()

# Con parametros y sin retorno
def hello2(name):
    print("hello",name)

hello2("Python")
hello2("Java")
hello2("HTML")
hello2("CSS")

# Funciones con parametros y con retorno
def duplica(num):
    return num * 2

doble = duplica(15)
print(f"El doble de 15 es:",doble)

def suma(num1,num2):
    return num1 + num2
resul = suma(16 - 20)
print(resul)

def fullname(name, ap_pat, ap_mat):
    return f"{name} {ap_pat} {ap_mat}"

print(fullname("Edgar", "David", "Corona"))
print(fullname("David", "Corona", "Edgar"))
print(fullname("David", "Edgar", "Corona"))

# Parámetros nombrados correctamente
print(fullname(ap_pat="Corona",
               ap_mat="Edgar",
               name="David"))

# Parametros opcionales 

def get_hero(name, hero = "superman"):
    return f"{name} is {hero}"

print(get_hero("Edgar"))
print(get_hero("Pepito"))
print(get_hero("Carlitos"))

