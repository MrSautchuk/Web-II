#18) Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

#19) Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

conjunto = []
n = int(input("Quantos numeros quer adicionar ao conjunto de numeros? "))
maior = 0
menor = 1001


for i in range(n):
  numero = int(input(f"Digite um numero inteiro maior que 0: "))
  if numero > 0 and numero < 1000:
    conjunto.append(numero)
    if maior < numero:
      maior = numero
    
    if menor > numero:
      menor = numero
    
  else:
    print("Você deve inputar numeros dentro do intervalo (0 / 1000)")

if n == len(conjunto):
  print(f"Foi imputado o seguinte conjunto {conjunto}")
  print(f"O conjunto possui {len(conjunto)} numeros")
  print(f"O maior deles é o numero {maior}")
  print(f"O menor deles é o numero {menor}")