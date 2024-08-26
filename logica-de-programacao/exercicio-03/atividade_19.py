score1 = int(input("Digite a primeira nota: "))
score2 = int(input("Digite a segunda nota: "))
score3 = int(input("Digite a terceira nota: "))

score1WithWeight = score1 * 2
score2WithWeight = score2 * 3
score3WithWeight = score3 * 5

amount = (score1WithWeight + score2WithWeight + score3WithWeight) / (2 + 3 + 5)

print(f"A média ponderada das notas é: {amount}")
