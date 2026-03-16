#24) Faça um programa que calcule o mostre a média aritmética de N notas.

notas = []
n = int(input("quantas notas deseja incluir? "))
i = 0
soma = 0

while i < n:
  entrada = float(input("entre com a nota: "))
  notas.append(entrada)
  soma += notas[i]
  i += 1

media = soma / n

print(f"As notas digitadas foram: {notas}")
print(f"A media de todas elas é {media}")