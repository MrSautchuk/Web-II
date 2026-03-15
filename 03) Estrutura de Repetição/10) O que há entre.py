#10) Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

#11) Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Entre com um numero inteiro qualquer: "))
num2 = int(input("Entre com outro numero inteiro qualquer: "))
i = num1 + 1

while i < num2:
    print(i, end=" ")
    i += 1

print(" ")
print(f"A soma de todos os numeros dentro do ntervalo é: {num1 + num2}")