# Dada a lista de convidados convidados = ["Alice", "Bob",
# "Carlos", "Diana", "Eduardo"], crie um programa que
# imprima uma lista numerada no formato:

# 1. Alice

# 2. Bob

# ... e assim por diante.

lista = ["Alice", "Bob", "Carlos", "Diana", "Eduardo"]

for i in range(len(lista)):
    print(f"{i + 1}. {lista[i]}")