#15) Faça um Programa que pergunte quanto você ganha por hora          ok
# e o número de horas trabalhadas no mês.                              ok
# Calcule e mostre o total do seu salário no referido mês,             ok 
# sabendo-se que são descontados                                       ok
# 11% para o Imposto de Renda,                                         ok
# 8% para o INSS e                                                     ok
# 5% para o sindicato,                                                 ok
# faça um programa que nos dê:                                         ok
#	-salário bruto.                                                      ok
#	-quanto pagou ao INSS.                                               ok
#	-quanto pagou ao sindicato.                                          ok
#	-o salário líquido.                                                  ok
#	calcule os descontos e o salário líquido, conforme a tabela abaixo:
#	+ Salário Bruto : R$                                                 ok
#	- IR (11%) : R$                                                      ok
#	- INSS (8%) : R$                                                     ok
#	- Sindicato ( 5%) : R$                                               ok
#	= Salário Liquido : R$                                               ok
#	Obs.: Salário Bruto - Descontos = Salário Líquido.                   ok

HR = float(input("Quanto você ganha por hora? "))
hrs_trabalhadas = float(input("Quantas horas trabalha por mês?"))
salario_bruto = hrs_trabalhadas * HR
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = IR + INSS + sindicato
salario_liquido = salario_bruto - descontos

print("De acordo com o que você ganha por hora (R$", HR, " reais) e a quantidade de horas que trabalha por mês (", hrs_trabalhadas, ")")
print("Seu salário bruto é de : R$", salario_bruto)
print("Considerando os seguintes descontos: ")
print("imposto de renda R$ ", IR, " reais")
print("INSS R$", INSS, " reais")
print("Sindicato R$ ", sindicato, " reais")
print("Totalizando em : R$", descontos, " reais")
print("O seu salário liquido é de : R$ ", salario_liquido)