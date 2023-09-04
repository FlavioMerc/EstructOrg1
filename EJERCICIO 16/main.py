
lote = int(input('Digite tamaño de lote: '))

i = 1
aptas = 0
while i <= lote:
    pieza = float (input(f"Ingrese la longitud de la pieza {i}: "))

    if pieza >= 1.20 and pieza <= 1.30:
        aptas += 1

    i += 1

print(f"Las piezas aptas son {aptas}")



