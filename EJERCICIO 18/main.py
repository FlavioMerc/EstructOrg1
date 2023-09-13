numero = int(input('Digite un numero: '))
factorial = 1

for i in range(1,(numero + 1)):
    if i <= 1:
        factorial = 1
    else:
        factorial = i * factorial

print("El factorial es: ", factorial)