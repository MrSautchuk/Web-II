# Imagine que você recebeu uma lista de preços de produtos:
# precos = [10.50, 150.00, 45.00, 210.90, 85.00, 300.00]. Crie
# um programa que percorra essa lista e gere uma nova lista
# chamada produtos_premium contendo apenas os valores
# acima de R$ 100,00. Ao final, exiba a nova lista.

precos = [10.50, 150.00, 45.00, 210.90, 85.00, 300.00]

for i in range(len(precos)):
    if precos[i] > 100:
        prodrutosPremium = [precos[i]]

print(prodrutosPremium)