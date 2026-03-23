

def temperatura_media(tem1, tem2):
    return (tem1, tem2)/2

if __name__ == "__main__":
    temps = int("cuantas tamperaturas vas a calcular")
    for i in temps:
        temps1 = float(input("ingresa la tamperatura minima"))
        temps2 = float(input("ingresa la tamperatura maxima"))

        print(f'la temperatura meda es {temperatura_media(temps1, temps2) }')
        