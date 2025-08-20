mayor = 0

while True:
    edad = input("Ingresa una edad (si quieres salir, escribe -1): ")
    if edad == "-1":
        break
    if int(edad) > mayor:
        mayor = int(edad)

print("La edad mayor ingresada es:", mayor)