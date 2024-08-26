import random

drawn_number = random.randint(1, 1000)

while True:
    num = int(input("Escolha um número entre 1 e 1000: "))

    if num == drawn_number:
        break

    if num < drawn_number:
        print("O número sorteado é maior que seu número, tente novamente!")        

    if num > drawn_number:
        print("O número sorteado é menor que seu número, tente novamente!")       

print("Você acertou o número!")