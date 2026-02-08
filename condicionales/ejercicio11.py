

#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las 
#dimensiones de los lados de un triángulo. 
#El programa debe determinar que tipo de triángulo es, teniendo en cuenta:
#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

A = int(input("Lado 1 del triangulo: "))
b = int(input("Lado 2 del triangulo: "))
c = int(input("Lado 3 del triangulo: "))

if A**2 + B**2 == C**2 or B**2 + C**2 == A**2 or C**2 + A**2 == B**2:
    print("Triángulo Rectángulo")

if (A == B and A != C) or (B == C and B != A) or (C == A and C != B):
    print("Triángulo Isósceles")
else:
    if A == B and A == C:
        print("Triángulo Equilátero")
    else:
        print("Triángulo Escaleno")