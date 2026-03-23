def centrar(cadena):
    espacios = (40 - len(cadena)) // 2
    message = " " * espacios + cadena
    print(message)
    separacion = " " * espacios + "=" * len(cadena)
    print(separacion)


if __name__ == "__main__":
    message_1 = input("Coloca un texto: ")
    message_2 = input("Coloca otro texto: ")
    print()
    centrar(message_1)
    centrar(message_2)
