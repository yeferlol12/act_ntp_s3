import random

numero_secreto = random.randint(1, 10)
adivinanza = 0

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (1-10): "))

print(" Adivinaste el número", numero_secreto)