#Escreva um programa que utilize o laço for e a função 
# range() para imprimir todos os números múltiplos de 3, no
# intervalo de 1 a 50, em ordem decrescente (do maior para o menor).

for i in range(50):
    if i % 3 == 0:
        print(i)