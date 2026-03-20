#08) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hr = int(input("Quanto você cobra por hora? "))
hr_trabalhada = int(input("Quantas horas trabalha em um mês? "))
mensal = hr * hr_trabalhada

print("Se sua hora vale ", hr, " e você trabalha ", hr_trabalhada, " em um mês")
print("Então você ganha ", mensal, " em um mês")