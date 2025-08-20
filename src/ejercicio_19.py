
frase = "programacion es divertida"
vocales = "aeiou"
contador = 0

for letra in frase:
    if letra.lower() in vocales:
        contador = contador + 1

print("El total de vocales es:", contador)