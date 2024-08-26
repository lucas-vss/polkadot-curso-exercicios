count = 0
score = 0
amount = 0

print("Digite -1 para parar de obter as notas e calcular a média")

while True:
    score = float(input("Digite a nota: "))
    
    if score == -1:
        break
    
    amount += score
    count += 1

media = amount / count

print(f"A média das notas foi: {media}")