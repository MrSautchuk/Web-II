# 35) Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

num = int(input("Entre com um numero, vou calcular quantos numeros primos existem de 0 ate o numero digitado: \n"))
lista = []

def primo(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    
    limite = int(n ** 0.5) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
            
    return True

for i in range(2, num + 1):
    if primo(i):
        lista.append(i)

print(lista)