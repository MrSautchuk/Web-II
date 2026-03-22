# 32) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

num = int(input("Entre com o numero que deseja calcular o fatorial: \n"))
fat = num

for i in range(num - 1):
  fat = fat * (num - 1)
  num -= 1

print(fat)