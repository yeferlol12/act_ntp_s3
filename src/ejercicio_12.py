n = int(input("Ingresa un número entero: "))
resultado = 1
contador = 1

while contador <= n:
    resultado = resultado * contador
    contador = contador + 1

print("El factorial de", n, "es:", resultado)