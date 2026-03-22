# 34) Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

def primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = int(n ** 0.5) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
            
    return True

numero = int(input("Digite um número inteiro: "))
if primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")