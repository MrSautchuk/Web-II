#Crie um programa que receba uma frase do usuário 
# e conte quantas vogais (a, e, i, o, u) ela possui. O programa
# deve exibir o total ao final.

frase = input("Digite uma frase curta qualquer: \n").lower

vogais = "aeiou"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"A frase possui {contador} vogais.")
