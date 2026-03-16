#21) Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

#22) Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

n = int(input("Digite um número inteiro N: "))
primos = []
total_divisoes = 0

for num in range(2, n + 1):
    eh_primo = True
    
    if num == 2:
        primos.append(2)
        continue
        

    total_divisoes += 1
    if num % 2 == 0:
        continue
        

    raiz = int(num ** 0.5)
    for i in range(3, raiz + 1, 2):
        total_divisoes += 1
        if num % i == 0:
            eh_primo = False
            break 
            
    if eh_primo:
        primos.append(num)

print(f"\nNúmeros primos entre 1 e {n}:")
print(primos)
print(f"Total de divisões executadas: {total_divisoes}")