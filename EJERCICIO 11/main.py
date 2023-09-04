compra = float(input('Digite el monto de la compra: '))

if compra > 400 :
    print("Pagara: ",(compra-(compra*0.15))," por su compra")
else:
    print("Pagara: ",compra," por su compra")

print("Fin del Programa")