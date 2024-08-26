amount = 0

for i in range(1, 101):
    if (i % 2 == 0):
        amount += i

print(f"A soma acumulada dos número pares é: {amount}")