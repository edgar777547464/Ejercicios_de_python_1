

import random
numero = []

for i in range(10):
    numero.append(random.randint(1,10))

for n in numero:
    print(n, "su cuadrado:",n**2,"su cubo",n**3)
