print("Para receber o resultado digite SAIR")

numbers = []

while True:
    num = input("Digite um número: ")

    if num == "SAIR":
        break
    
    numbers.append(int(num))

minor = numbers[0]
major = numbers[0]
amount = numbers[0]

for number in numbers[1:]:
    if number < minor:
        minor = number
    
    if number > major:
        major = number

    amount += number


print(f"O menor número fornecido foi: {minor}")
print(f"O maior número fornecido foi: {major}")
print(f"A soma de todos os número fornecidos foi: {amount}")
