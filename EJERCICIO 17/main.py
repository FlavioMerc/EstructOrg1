
aprobados = 0
reprobados = 0
i = 1
while i <= 10:
    calificacion = int (input(f"Ingrese la calificacion {i}: "))

    if calificacion >= 70:
        aprobados += 1
    else:
        reprobados += 1
    
    i += 1

print(f"La calificaciones menores a 70 son : {reprobados}")
print(f"Las calificaciones mayores a 70 son : {aprobados}")
