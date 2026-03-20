#06) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = int(input("Qual o raio do circulo? "))
π = 3.14
area =  π * (raio**2)

print("Se o raio do circulo é de ", raio)
print("Então o elevamos ao quadrado resultando em ", raio**2)
print("e multiplicamos isso por PI, resultando em ", area, " que é a area do circulo.")