factorial = 1

num = int(input("Digite um número: "))


for i in range(1, num + 1):
    factorial *= i

print(f"O fatorial de {num} é: {factorial}")