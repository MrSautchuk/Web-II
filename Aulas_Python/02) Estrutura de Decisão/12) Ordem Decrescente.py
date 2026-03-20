#12) Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite um numero inteiro qualquer: "))
num2 = int(input("Digite um mais numero inteiro qualquer: "))
num3 = int(input("Digite um mais numero inteiro qualquer: "))
maior = 0
medio = 0
menor = 0


if (num1 > num2) and (num1 > num3):
  maior = num1
elif (num2 > num1) and (num2 > num3):
  maior = num2
elif (num3 > num1) and (num3 > num2):
  maior = num3

if (num1 < num2) and (num1 < num3):
  menor = num1
elif (num2 < num1) and (num2 < num3):
  menor = num2
elif (num3 < num1) and (num3 < num2):
  menor = num3

if (num1 < maior) and (num1 > menor):
  medio = num1
elif (num2 < maior) and (num2 > menor):
  medio = num2
elif (num3 < maior) and (num3 > menor):
  medio = num3

print("Os numeros digitados foram: ", num1, num2, num3)
print("A exibição em ordem decrescente é:")
print(maior, medio, menor)