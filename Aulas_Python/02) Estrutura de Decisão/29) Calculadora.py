#29) Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#	-par ou ímpar;
#	-positivo ou negativo;
#	-inteiro ou decimal.

num1 = float(input("Entre com o primeiro numero: \n"))
num2 = float(input("Entre com o segundo numero: \n"))
operacao = int(input("Que tipo de operação deseja realizar? \n(1) Soma \n(2) Subtração \n(3) Multplição \n(4) Divisão"))
soma = num1 + num2
multiplicacao = num1 * num2
subtracao = num1 - num2
divisao = num1 / num2
modulo = num1 % num2
paridade = ""
sinal = ""
conjunto = ""

if (operacao == 1):
  print(num1, "+", num2,"=",soma)
  if (soma > 0):
    print(soma, " é um numero positivo")
  else:
    print(soma, " é um numero negativo")
  if ((soma%2) == 0):
    print(soma, " é um numero par")
  else:
    print(soma, " é um numero impar")
  if (soma == round(soma)):
    print(soma, " é um numero inteiro")
  else:
    print(soma, " é um numero decimal")
elif (operacao == 2):
  print(num1, "-", num2,"=",subtracao)
  if (subtracao > 0):
    print(subtracao, " é um numero positivo")
  else:
    print(subtracao, " é um numero negativo")
  if ((subtracao%2) == 0):
    print(subtracao, " é um numero par")
  else:
    print(subtracao, " é um numero impar")
  if (subtracao == round(subtracao)):
    print(subtracao, " é um numero inteiro")
  else:
    print(subtracao, " é um numero decimal")
elif (operacao == 3):
  print(num1, "*", num2,"=",multiplicacao)
  if (multiplicacao > 0):
    print(multiplicacao, " é um numero positivo")
  else:
    print(multiplicacao, " é um numero negativo")
  if ((multiplicacao%2) == 0):
    print(multiplicacao, " é um numero par")
  else:
    print(multiplicacao, " é um numero impar")
  if (multiplicacao == round(multiplicacao)):
    print(multiplicacao, " é um numero inteiro")
  else:
    print(multiplicacao, " é um numero decimal")
elif (operacao == 4):
  print(num1, "/", num2,"=",divisao, " com resto ", modulo)
  if (divisao > 0):
    print(divisao, " é um numero positivo")
  else:
    print(divisao, " é um numero negativo")
  if ((divisao%2) == 0):
    print(divisao, " é um numero par")
  else:
    print(divisao, " é um numero impar")
  if (divisao == round(divisao)):
    print(divisao, " é um numero inteiro")
  else:
    print(divisao, " é um numero decimal")