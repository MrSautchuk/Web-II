#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

divida = float(input("Digite o valor da dívida: R$ "))

print("\nValor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")
opcoes = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]

for parcelas, perc_juros in opcoes:
    valor_juros = divida * (perc_juros / 100)
    divida_total = divida + valor_juros
    valor_parcela = divida_total / parcelas
    
    print(f"R$ {divida_total:<12.2f} | R$ {valor_juros:<13.2f} | {parcelas:<22} | R$ {valor_parcela:.2f}")