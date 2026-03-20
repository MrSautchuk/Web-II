#34) O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#	                Até 5 Kg           Acima de 5 Kg
#	File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#	Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#	Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

#35) Para atender a todos os clientes, 
# cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 		ok
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 		ok
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário 		ok
# e gere um cupom fiscal, 
# contendo as informações da compra: 
# tipo e quantidade de carne, 
# preço total, 
# tipo de pagamento, 
# valor do desconto 
# e valor a pagar.

print("O Hipermercado Tabajara esta com ofertas especiais \n")
print("                Até 5 Kg           Acima de 5 Kg")
print("File Duplo      R$ 4,90 por Kg      R$ 5,80 por Kg")
print("Alcatra         R$ 5,90 por Kg      R$ 6,80 por Kg")
print("Picanha         R$ 6,90 por Kg      R$ 7,80 por Kg")
print("Para atender a todos os clientes a compra está limitada a apenas um item, idependente da quantidade \n")

carne = ""
tipoCarne = int(input("Qual item do açougue gostaria? \n (1) File Duplo \n (2) Alcatra \n (3) Picanha \n"))
KG = float(input(f"Quantos quilos deseja levar de {carne}"))

if tipoCarne == 1 or tipoCarne == 2 or tipoCarne == 3:
	if tipoCarne == 1:
		carne = "File Duplo"
		if KG < 5:
			valorCarne = 4.9
		else:
			valorCarne = 5.8
	elif tipoCarne == 2:
		carne = "Alcatra"
		if KG < 5:
			valorCarne = 5.9
		else:
			valorCarne = 6.8
	elif tipoCarne == 3:
		carne = "Picanha"
		if KG < 5:
			valorCarne = 6.9
		else:
			valorCarne = 7.8

	pagamento = input("O pagamento sera realizado utilçizando o cartão Tabajara? (s/n) \n").lower
	subTotal = KG * valorCarne

	if pagamento == "s":
		total = (subTotal * 0.05) + subTotal
	else:
		total = subTotal

	if KG < 5:
		descontos = 0.9 + total - subTotal
	else:
		descontos = total - subTotal

else:
	print("Opção invalida")

print(f"|============== Cupom Fiscal ====================================|")
print(f"|Produto......Quantidade.....Preço......Subtotal                 |")
print(f"|{carne}.....{KG}kg.........R${valorCarne}....R${valorCarne * KG}                   |")
print(f"|Descontos....{descontos}                                                |")
print(f"|Total.....{total}                                                  |")
