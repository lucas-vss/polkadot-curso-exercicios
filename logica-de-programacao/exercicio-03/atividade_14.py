num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operation = input("Digite qual a operação que você deseja. ex (+ | - | * | /): ")

match operation:
    case '+':
        result = num1 + num2
        print(f"O resultado da soma é: {result}")
    case '-':
        result = num1 - num2
        print(f"O resultado da subtração é: {result}")
    case '*':
        result = num1 * num2
        print(f"O resultado da multiplicação é: {result}")
    case '/':
        result = num1 / num2
        print(f"O resultado da divisão é: {result}")
    case _:
        print("Operação inválida")