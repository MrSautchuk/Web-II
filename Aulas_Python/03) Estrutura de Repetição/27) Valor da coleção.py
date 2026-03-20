#27) Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade = int(input("Quantos CDs tem sua coleção? "))
loop = 1
total = 0

while loop <= quantidade:
  input(f"Qual o {loop}º CD? ")
  preco = float(input("Quanto pagou por ele? R$"))
  total += preco
  loop += 1

media = total / quantidade

print(f"Sua coleção possui {quantidade} CDs e te custou R${total}")
print(f"O custo médio de cada CD da coleção é de R${media}")