Valor_Venta = float(input('Digite el valor de venta: '))
Motos_Vend = int(input('Digite el numero de motos vendidas: '))

Comision = 200*Motos_Vend
Porcentaje = (Valor_Venta * 0.05)
Salario = 2000 + Comision + Porcentaje

print("Su salario mensual es: ",Salario)