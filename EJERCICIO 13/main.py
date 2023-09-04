numeroUno = int(input('Digite un numero entero: '))
numeroDos = int(input('Digite un numero entero: '))

if numeroUno % 2 == numeroDos % 2:
    print("Los numeros son pares")
elif (numeroUno % 2 != numeroDos % 2 ) :
    print("Los numeros son impares")
else :
    print("Un numero es par y el otro impar")

