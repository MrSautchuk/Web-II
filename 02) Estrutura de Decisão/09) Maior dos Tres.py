#09) Faça um Programa que leia três números e mostre o maior deles.

num1 = input("Digite um numero qualquer (apenas numeros): ")
num2 = input("Digite um outro qualquer (apenas numeros): ")
num3 = input("Digite um outro qualquer (apenas numeros): ")

if (num1.isnumeric()) and (num2.isnumeric()) and (num3.isnumeric()):
  if (float(num1) > float(num2)) and (float(num1) > float(num3)):
    print(num1, " é o maior dos três.")
  elif (float(num2) > float(num1)) and (float(num2) > float(num3)):
    print(num2, " é o maior dos três")
  else:
    print(num3, " é o maior dos três")
else:
  print("O que você digitou não são numeros.")