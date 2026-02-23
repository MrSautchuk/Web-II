#18) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

import math

tamanho = float(input("Qual o tamanho do arquivo em MB? (somente numeros) "))
velocidade = float(input("Quantos Megabits de velocidade tem a internet? (somente numeros) "))
velocidadeReal = velocidade / 8
tempo = math.ceil((tamanho / velocidadeReal) / 60)

print("O download vai levar aproximadamente ", tempo , " minutos")