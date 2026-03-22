# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.
# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.

n_termos_S = int(input("\nSérie S - Digite a quantidade de termos (n): "))
soma_S = 0
m = 1
for i in range(1, n_termos_S + 1):
    soma_S += i / m
    m += 2
print(f"Soma da Série S: {soma_S:.2f}")

n_termos_H = int(input("\nSérie H - Digite a quantidade de termos (N): "))
soma_H = 0
for i in range(1, n_termos_H + 1):
    soma_H += 1 / i
print(f"Soma da Série H: {soma_H:.2f}")