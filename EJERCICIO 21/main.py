positivo = 0
negativo = 0
i = 1
for i in range (10):
    numero = float(input('Digite el numero {i}: '))
    if numero >= 0:
        positivo += 1
    else:
        negativo += 1
    
    i += 1
print("positivos: ",positivo)
print("negativos: ",negativo)