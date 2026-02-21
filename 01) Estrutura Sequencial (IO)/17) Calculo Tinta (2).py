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

MT = float(input("Quantos metros quadrados pretende pintar? "))
necessario = (MT / 6) *1.10
necessarioLata = necessario / 18
necessarioGalao = necessario / 3.6
valorLata = 80.00
valorGalao = 25.00

print("===========================================================")

print("Você vai pintar ", MT, " Metros quadrados")
print("e vai precisar de ", necessario, " Litros de tinta")

print("===========================================================")

print("Caso opite pela lata de 18 lts de tinta:")
print("Serão necessárias ", necessarioLata, " latas de tinta")
print("Você terá um custo total de R$", valorLata * necessarioLata)

print("===========================================================")

print("Caso opite pelo Galão de 3,6 lts de tinta:")
print("Serão necessárias ", necessarioGalao, " latas de tinta")
print("Você terá um custo total de R$", valorLata * necessarioGalao)

print("===========================================================")

print("Caso opite comprar latas e galões:")
print("Serão necessárias ", necessarioLata // MT, " latas de tinta")
print("Serão necessárias ", necessarioLata % MT, " latas de tinta")
print("Você terá um custo total de R$", (((necessarioLata // MT) * valorLata) + ((necessarioLata % MT) * valorGalao)))