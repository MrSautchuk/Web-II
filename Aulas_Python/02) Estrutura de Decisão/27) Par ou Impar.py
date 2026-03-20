#27) Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

num = int(input("Entre com um numero inteiro qualquer:\n"))
verificacao = num % 2

if (verificacao == 0):
  print("O numero digitado é par")
else:
  print("O numero digitado é impar")