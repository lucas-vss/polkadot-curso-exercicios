def is_prime(num):
    if num <= 1:
        return False
    
    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


print("Defina um intervalo")

smallest_number = int(input("Digite o menor número do intervalo: "))
greatest_number = int(input("Digite o maior número do intervalo: "))

if smallest_number < greatest_number:
    for i in range(smallest_number, greatest_number + 1):
        if is_prime(i):
            print(f"{i} é um número primo")
        else:
            print(f"{i} não é um número primo")
else:
    print("Intervalo inválido")