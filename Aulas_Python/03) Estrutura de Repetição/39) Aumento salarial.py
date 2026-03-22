# 39) Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# 	-Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# 	-Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# 	-A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario = float(input("Entre como o salario inicial: "))
aumento = 0.015
dataInicial = int(input("Em qual ano iniciou suas atividades neste emprego? "))
dataFinal = int(input("Ate que ano trabalhou neste emprego? "))
periodo = dataFinal - dataInicial

for i in range(periodo):
  salario = (salario * aumento) + salario
  aumento = aumento * 2
  print(f"{i}, {salario}, {aumento}")