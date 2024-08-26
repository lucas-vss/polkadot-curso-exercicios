num = int(input("Digite um número para ver sua sequência de Fibonacci: "))

fibonacci_sequence = []
first, second = 0, 1

while len(fibonacci_sequence) < num:
    fibonacci_sequence.append(first)
    first, second = second, first + second
    
print(f"A sequência de Fibonacci até {num} é: ")
print(fibonacci_sequence) 