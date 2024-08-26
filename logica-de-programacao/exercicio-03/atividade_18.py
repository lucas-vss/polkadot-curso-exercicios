phrase = input("Digite uma frase qualquer: ")

words = []
index = 0

for i in range(0, len(phrase)):
    if phrase[i] == ' ':
        words.append(phrase[index:i])
        index = i

print(f"A quantidade de palavras na frase é: {len(words)}")