#17) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 

# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que 

# a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou 
# em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#	-comprar apenas latas de 18 litros;
#	-comprar apenas galões de 3,6 litros;
#	-misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#====================================================================================================#

#=====================================  Não está pronto  ============================================#

#====================================================================================================#
import math


MT = float(input("|        Quantos metros quadrados pretende pintar?        |"))
necessario = (MT / 6) *1.10
necessarioLata = necessario / 18
necessarioGalao = necessario / 3.6
valorLata = 80.00
valorGalao = 25.00

print("===========================================================")

print("Você vai pintar ", MT, " Metros quadrados")
print("Contando com 10% de margem para não faltar")
print(f"Você vai precisar de {necessario:.2f} Litros de tinta")

print("===========================================================")

# print("Caso opite pela lata de 18 lts de tinta:")
# print("Serão necessárias ", math.ceil(necessarioLata), " latas de tinta")
# print("Você terá um custo total de R$", valorLata * math.ceil(necessarioLata))
# print(f"Terá um desperdício de {(math.ceil(necessarioLata)*18) - necessario:.2f} litros")

# print("===========================================================")

# print("Caso opite pelo Galão de 3,6 lts de tinta:")
# print("Serão necessárias ", math.ceil(necessarioGalao), " galões de tinta")
# print("Você terá um custo total de R$", valorGalao * math.ceil(necessarioGalao))
# print(f"Terá um desperdício de {(math.ceil(necessarioGalao)*3.6) - necessario:.2f} litros")

# print("===========================================================")

print("Caso opite entre latas e galões visando evitar o desperdicio:")
print("Serão necessárias ", math.floor(necessarioLata), " latas de tinta")
print(f"Faltando  {necessario % 18:.2f} litros a serem completados com galões")
print("Serão necessários ", math.ceil(necessario % 18 / 3.6), " galões de tinta")
print("Você terá um custo total de R$", (math.floor(necessarioLata) * 80.00) + (math.floor(necessarioLata) * 25.00))