

def numneros(num1, num2):
    #residuo = num1 % num2
    #if residuo == 0:
    #    return True
    #else:
    #    return False
    
    return num1 % num2 ==0

if __name__ == "__main__":
    num1 = int(input("ingresa un numero: "))
    num2 = int(input("colca otro numero:"))

    if numneros(num1, num2):
        print(f'{num1} es multiplo de {num2}')
    else:
        print(f'{num1} no es multiplo de {num2}')

        