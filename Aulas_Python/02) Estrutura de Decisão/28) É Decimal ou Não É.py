#28) Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = float(input("informe um numero qualquer: \n"))

if (num == round(num)):
  print(num, " é um numero inteiro")
else:
  print(num, " é um numero decimal")