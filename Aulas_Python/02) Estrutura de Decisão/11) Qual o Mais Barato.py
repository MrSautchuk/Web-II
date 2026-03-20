#11) Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

banana = float(input("Quanto está o kg da banana hoje? "))
maca = float(input("Quanto está o kg da maçã hoje? "))
abacaxi = float(input("Quanto está o kg do abacaxi hoje? "))

if (banana < maca) and (banana < abacaxi):
  print("Você deveria aproveitar o preço e comprar Bananas hoje")
elif (maca < banana) and (maca < abacaxi):
  print("Você deveria aproveitar o preço e comprar Maçãs hoje")
else:
  print("Você deveria aproveitar o preço e comprar Abacaxis hoje")