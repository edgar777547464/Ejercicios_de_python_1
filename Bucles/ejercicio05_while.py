
caracter = input('Escribe una letra (" " para salir): ')

while caracter != " ":
    if len(caracter) == 1:  # Aseguramos que sea solo un carácter
        if caracter.upper() in ['A', 'E', 'I', 'O', 'U']:
            print("Vocal")
        else:
            print("No vocal")
    else:
        print("Por favor escribe solo un carácter.")

    caracter = input('Escribe una letra (" " para salir): ')
    
