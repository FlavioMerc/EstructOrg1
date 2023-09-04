hora = int(input('Digite el numero de horas trabajadas: '))

if hora < 40 :
    print('Su salario es: ',(hora*190))
else:
    print('Su salario es:',(40*190)+((hora-40)*210))

print("Fin del Programa")