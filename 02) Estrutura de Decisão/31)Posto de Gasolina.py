#31) Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#	Álcool:
#	-até 20 litros, desconto de 3% por litro
#	-acima de 20 litros, desconto de 5% por litro
#	Gasolina:
#	-até 20 litros, desconto de 4% por litro
#	-acima de 20 litros, desconto de 6% por litro 

# Escreva um algoritmo que leia o número de litros vendidos, 
# 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

print("TABELA DE DESCONTOS")
combustivel = input("Qual combustivel deseja abastecer? \n(A) Alcool - (G) Gasolina\n").upper()
litros = float(input("Quantos litros deseja abastecer?"))
alcool = 1.9
gasolina = 2.5

if (combustivel == "A"):
  if (litros <= 20):
    print("O desconto aplicado será de 3% (R$ ", round((litros * alcool) * 0.03, 2), ")")
    print(litros, " de Alcool abastecidos")
    print("O valor a ser pago é: R$", round(((litros * alcool) * 0.03) + (litros * alcool), 2))
  elif (litros > 20):
    print("O desconto aplicado será de 5% (R$ ", round((litros * alcool) * 0.05, 2), ")")
    print(litros, " de Alcool abastecidos")
    print("O valor a ser pago é: R$", round(((litros * alcool) * 0.05) + (litros * alcool), 2))
elif (combustivel == "G"):
  if (litros <= 20):
    print("O desconto aplicado será de 4% (R$ ", round((litros * gasolina ) * 0.04, 2), ")")
    print(litros, " de Gasolina abastecidos")
    print("O valor a ser pago é: R$", round(((litros * gasolina ) * 0.04) + (litros * gasolina), 2))
  elif (litros > 20):
    print("O desconto aplicado será de 6% (R$ ", round((litros * gasolina ) * 0.06, 2), ")")
    print(litros, " de Gasolina abastecidos")
    print("O valor a ser pago é: R$", round(((litros * gasolina ) * 0.06) + (litros * gasolina), 2))
else:
  print("O que disse???")
  print("Tente novamente")