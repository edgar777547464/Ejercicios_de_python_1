

#ejercicio que pida vocales que pida caracteres e imprima "VOCAl"si son vocales
#en caso contrario, el programa 

caracterer = input('Escribe una letra(" " para salir)')

while True:
	caracterer = input('Escribe una letra (" " para salir): ')

	if caracterer == ' ':
		break


	if len(caracterer) == 1:
		if caracterer.upper() == 'A' \
			or caracterer.upper() == 'E' \
			or caracterer.upper() == 'I' \
			or caracterer.upper() == 'O' \
			or caracterer.upper() == 'U' \
			print('Vocal')
		else:
			print("no vocal")

	if caracterer == ' ':
		break

	
