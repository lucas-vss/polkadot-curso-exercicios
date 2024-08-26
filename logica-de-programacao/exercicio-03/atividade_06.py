vowels = ['a', 'e', 'i', 'o', 'u']

phrase = input("Digite uma frase: ")

count = 0

for character in phrase:
    if character in vowels:
        count += 1

print(f"A frase contém {count} vogais")