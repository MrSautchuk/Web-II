# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

int1 = int2 = int3 = int4 = 0

while True:
    num = int(input("Digite um número (negativo para sair): "))
    if num < 0:
        break
    
    if 0 <= num <= 25:
        int1 += 1
    elif 26 <= num <= 50:
        int2 += 1
    elif 51 <= num <= 75:
        int3 += 1
    elif 76 <= num <= 100:
        int4 += 1

print(f"[0-25]: {int1} | [26-50]: {int2} | [51-75]: {int3} | [76-100]: {int4}")