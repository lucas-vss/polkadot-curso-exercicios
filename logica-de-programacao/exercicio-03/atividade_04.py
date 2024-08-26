def is_palindrome(word):
    first_index = 0
    last_index = len(word) - 1

    while first_index < last_index:
        if word[first_index] != word[last_index]:
            return False
        first_index += 1
        last_index -= 1
    
    return True

word = input("Digite a palavra: ")

if is_palindrome(word):
    print("A palavra é palindroma")
else:
    print("A palavra não é palindroma")