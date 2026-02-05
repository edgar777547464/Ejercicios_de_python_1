

# Datos los catetos de un triangulo rectangulo,
# calcular su hipotenusa.

# hipotenusa^2 = cat_1^2 + cat_2^2

cateto_1 = int(input('Ingresa el Cateto 1: '))
cateto_2 = int(input('Ingresa el cateto 2: '))

hipotenusa = (cateto_1 ** 2 + cateto_2 ** 2) ** (1/2)

print("La hipotenusa es", hipotenusa)