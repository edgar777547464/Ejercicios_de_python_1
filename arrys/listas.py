

'''
Colecciones en Python

listas (list)

'''

my_list = [3, 1, 5, 7, 4, 5]
print(my_list)
print(type(my_list))
print(my_list[3])
print(my_list[0])
print(my_list[-1])
print(len(my_list))

my_otra_lista = ["hola", 2, True, [1, 2, 3]]
print(my_otra_lista[3][0])

for i in range(len(my_otra_lista)):
    print(i, "->",my_otra_lista[i])

for i in my_otra_lista:
    print(i)

numbers = [3, 4, 5, 5, 6, 2]

print(numbers)
numbers.append(20)
print(numbers)

numbers.sort()
print(numbers)

numbers.remove(4)
print(numbers)

numbers.pop()
print(numbers)

numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)
