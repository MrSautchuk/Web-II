#15) As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. 
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#	-salários até R$ 280,00 : aumento de 20%                      OK
#	-salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#	-salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#	-salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
#	-o salário antes do reajuste;
#	-o percentual de aumento aplicado;
#	-o valor do aumento;
#	-o novo salário, após o aumento.


salario = float(input("Qual o salário do colaborador?\n"))
aumento = 0


if (salario <= 280):
  aumento = 0.2
elif (salario > 280) and (salario <= 700):
  aumento = 0.15
elif (salario > 700) and (salario <= 1500):
  aumento = 0.1
elif (salario > 1500):
  aumento = 0.05

print("O salário atual d colaborador é de ", salario)
print("Portanto o aumento aplicado será de ", aumento)
print("O novo salário do colaborador será ", (salario * aumento)+salario)