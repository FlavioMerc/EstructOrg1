numero = int(input('Digite el numero: '))

if numero > 99999:
    print("numero fuera del rango")
elif numero > 9999:
    print("Tiene 5 cifras")
elif numero > 999:
    print("Tiene 4 cifras")
elif numero > 99:
    print("Tiene 3 cifras")
elif numero > 9:
    print("Tiene 2 cifras")
else:
    print("Tiene 1 cifra")