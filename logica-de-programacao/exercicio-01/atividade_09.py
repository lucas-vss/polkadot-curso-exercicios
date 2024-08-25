phrase = input("Digite uma frase: ")
letter = input("Qual letra você quer verificar a quantidade na frase? ")

count = 0

for character in phrase:
    if character == letter:
        count += 1

print(f"A letra {letter} apareceu {count} vezes na frase")