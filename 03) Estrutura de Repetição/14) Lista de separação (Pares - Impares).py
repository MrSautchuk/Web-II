#14) Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

pares = 0
somaDosPares = 0
impares = 0
somaDosImpares = 0
i = 0

lista = []
for i in range(10):
  numero = int(input(f"Digite o {i + 1}º maior que 0: "))
  lista.append(numero)
  if lista[i] % 2 != 0:
    impares += 1
    somaDosImpares += lista[i]
  elif lista[i] % 2 == 0:
    pares += 1
    somaDosPares += lista[i]

print()
print(f"Os numeros digitados foram: {lista} \n")
print(f"Foam digitados {pares} numeros pares \n")
print(f"Foram digitados {impares} numeros impares \n")
print(f"A soma de todos os impares digitados é: {somaDosPares} \n")
print(f"A soma de todos os pares digitados é: {somaDosImpares} \n")