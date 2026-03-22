#Exercício 1
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"Total de vogais: {contador}\n")


#Exercício 2
for i in range(48, 0, -3):
    print(i)
print()


#Exercício 3
convidados = ["Alice", "Bob", "Carlos", "Diana", "Eduardo"]

for indice, convidado in enumerate(convidados, start=1):
    print(f"{indice}. {convidado}")
print()


#Exercício 4
for _ in range(5):
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        print("Processamento interrompido\n")
        break
else:
    print("Sequência processada com sucesso\n")


#Exercício 5
precos = [10.50, 150.00, 45.00, 210.90, 85.00, 300.00]
produtos_premium = []

for preco in precos:
    if preco > 100.00:
        produtos_premium.append(preco)

print(f"Produtos premium: {produtos_premium}")