#14) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

KG = float(input("Quantos KG de peixe trouxe hoje seu João? (apenas números)"))
limite = 50
excesso = KG - 50
multa = excesso * 4.00

if (KG < 50):
  print("Seu João, hoje você trouxe ", KG, "kg de peixe")
  print("Este peso esta dentro do regulamento")
  print("Portanto, não há multa a ser paga.")
elif (KG > 50):
  print("Seu João, hoje você trouxe ", KG, "kg de peixe")
  print("Este peso ultrapassa o estipulado pelo regulamento em ", excesso)
  print("Portanto o valor da multa a ser pago é : R$", multa, " reais")
else:
  print("Seu João, voce entoru com dados incorretos, por favor, tente novamente.")