#07) Faça um programa que leia 5 números e informe o maior número.
#08) Faça um programa que leia 5 números e informe a soma e a média dos números.

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite mais um numero: "))
num3 = float(input("Digite mais um numero: "))
num4 = float(input("Digite mais um numero: "))
num5 = float(input("Digite mais um numero: "))
maior = 0
soma = num1 + num2 + num3 + num4 + num5
media = soma / 5

if maior < num1:
  maior = num1
if maior < num2:
  maior = num2
if maior < num3:
  maior = num3
if maior < num4:
  maior = num4
if maior < num5:
  maior = num5

print(maior)
print(soma)
print(media)