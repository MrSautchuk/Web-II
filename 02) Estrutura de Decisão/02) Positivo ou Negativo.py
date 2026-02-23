#02) Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input("Insira um numero qualquer: "))

if (num < 0):
  print("Você digitou ", num, ", que é um numero negativo")
elif (num > 0): 
  print("Você digitou ", num, ", que é um numero positivo")
else:
  print("Voce digitou 0")