shopping_list = list()

print("Digite SAIR quando quiser finalizar a lista de compras \n")

while True:
    item = input("Adicione um novo item na sua lista: ")

    if item == "SAIR":
        break

    shopping_list.append(item)

print("Lista de compras:")
print(shopping_list)