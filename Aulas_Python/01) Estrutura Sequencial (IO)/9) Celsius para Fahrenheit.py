#09) Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#		C = 5 * ((F-32) / 9).

F = float(input("Quantos graus quer converter? "))
C = 5 * ((F-32) / 9)

print("A conversão de ", F, " fahrenheit em celsius é: ", C)