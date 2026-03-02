#26) Faça um Programa para um caixa eletrônico.           OK
# O programa deverá perguntar ao usuário a valor do saque     OK
# e depois informar quantas notas de cada valor serão fornecidas.  
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.    OK
# O valor mínimo é de 10 reais e o máximo de 600 reais.         OK
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.     OK
#	Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#	Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


print("|===Caixa Eletronico===|")
print("Notas Disponiveis: R$1, R$5, R$10, R$50 e R$100")
print("Disponibilidade de saque min. 10 max. 600")
saque = int(input("Quanto deseja sacar?\n"))
centenas = saque // 100
dezenas = (saque % 100) // 10
unidades = saque % 10

print("O valor solicitado para saque foi de : R$ ", saque)
print("Serão disponibilizadas ", centenas, " Notas de R$ 100 ", dezenas, " Notas de R$ 10 e ", unidades, " Notas de R$ 1 reais")