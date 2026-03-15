#32) Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      	Até 5 Kg           Acima de 5 Kg
#	Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#	Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#33) Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.



morangoKg = float(input("Quanto quilos de morango deseja? \n"))
macaKg = float(input("quantos quilos de maçã  deseja? \n"))
morangoValor = 0.0
macaValor = 0.0
subTotal = 0.0

if morangoKg < 5 :
  morangoValor = morangoKg * 2.5
else:
  morangoValor = morangoKg * 2.2

if macaKg < 5 :
  macaValor = macaKg * 2.5
else:
  macaValor = macaKg * 2.2

if (morangoKg + macaKg) > 8 or (morangoValor + macaValor) > 25:
  subTotal = morangoValor + macaValor - ((morangoValor + macaValor) * 0.1)
else:
  subTotal = morangoValor + macaValor

print(f"Bacana meu consagrado! {morangoKg} KG de morango e {macaKg} KG de maçã ")
print(f"Isso tudo vai custar {subTotal}")
print(f"O valor pago recebe um total de {(morangoValor + macaValor) - subTotal:.2f} de desconto")