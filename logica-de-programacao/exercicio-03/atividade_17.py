import math

num = int(input("Digite um número: "))

if num <= 1:
    print("Não é um número mágico")
else:
    amount = 0
    
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if i != num:
                amount += i
            if i != 1 and i != num // i and num // i != num:
                amount += num // i

    if amount == num:
        print("É um número mágico")
    else:
        print("Não é um número mágico")