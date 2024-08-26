word = input("digite um palavra: ")
inverted_word = ""

for i in range(len(word) -1, -1, -1):
    inverted_word += word[i]

print(f"A palavra na forma invertida é: {inverted_word}")