total = 0
while True:
    n = input("In gresa un número si, quieres salir unde 0 para salir: ")
    if n == "0":
        break
    total += float(n)
print("Total:", total)