#17) Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e   OK
# a quantidade de horas trabalhadas no mês.                  OK
#	Desconto do IR:
#	-Salário Bruto até 900 (inclusive) - isento                OK
#	-Salário Bruto até 1500 (inclusive) - desconto de 5%       OK
#	-Salário Bruto até 2500 (inclusive) - desconto de 10%      OK
#	-Salário Bruto acima de 2500 - desconto de 20%             OK
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

liquido = 0
horas = float(input("Quantas horas você trabalhou este mês?\n"))
bruto = (float(input("E quanto você ganha por hora?\n"))*horas)
IR = 0
INSS = 0.1
FGTS = 0.11

if (bruto > 900) and (bruto <= 1500):
  IR = 0.05
elif (bruto > 1500) and (bruto <= 2500):
  IR = 0.1
elif (bruto > 2500):
  IR = 0.2
else:
  IR = 0
print("\n")
print("|======================================================|")
print("|  O valor da sua hora é ", bruto / horas)
print("|  Este mês você trabalhou ", horas, " horas ")
print("|  Seu rendimento bruto deste mês é de ", bruto)
print("|======================================================|")
print("|........Salário Bruto:.................: R$ ", bruto)
print("|........(-)IR (", IR *100, "%)................: R$ ", bruto * IR)
print("|........(-)INSS (", INSS * 100, "%)..............: R$ ", INSS * bruto)
print("|...........FGTS (11%)..................: R$", FGTS * bruto)
print("|...........Totatl de Descontos.........: R$", (IR * bruto)+(INSS * bruto)+(FGTS * bruto))
print("|...........Salário Liquido.............: R$ ", bruto - ((IR * bruto)+(INSS * bruto)))
print("|======================================================")