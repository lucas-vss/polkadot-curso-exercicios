num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

numbers = [num1, num2, num3]

for i in range(len(numbers)):
    if numbers[i] > numbers[len(numbers) - 1]:
        aux = numbers[i]
        numbers[i] = numbers[len(numbers) - 1]
        numbers[len(numbers) - 1] = aux

print(numbers)