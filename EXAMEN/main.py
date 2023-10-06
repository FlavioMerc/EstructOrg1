#Examen
longitud =  int(input('Digite el tamaño:'))

for i in range (0,longitud + 1):
    for j in range(0,longitud + 1):
        if i and j == i:
            print(i,end=" ")
        else:
            print(" 0",end=" ")
    print("")
    