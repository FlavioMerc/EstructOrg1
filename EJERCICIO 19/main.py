numero = int(input('Digite un numero: '))

a, b = 0, 1

if numero <= 0:
    print("Vuelva a ingresar un termino")
elif numero == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, numero):
        fibonacci = a + b
        print(fibonacci)
        a,b = b, fibonacci


# numero = int(input("Digite un numero: "))
# 0 1 1 2 3 5 8 13

# for i in range(serie + 1)
#    print(c end=" ")
#    c = a + b
#    b = c
#    a = c