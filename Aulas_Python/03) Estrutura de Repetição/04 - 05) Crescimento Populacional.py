#04) Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

#05) Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

a = int(input("Qual a população atial do país A?"))
b = int(input("Qual a população atual do país B? "))
crescimentoA = float(input("Qual a taxa de cresciemnto do país A?"))
crescimentoB = float(input("Qual a taxa de cresciemnto do país B?"))
anos = 0

while a <= b :
  a = a + (a * crescimentoA)
  b = b + (b * crescimentoB)
  anos += 1

print(f"Será necessários {anos} anos para o pais A ultrapassar o pais B em crescimento populacional")
print(f"Em {anos} anos o país A estará na ordeem de {a:.0f} habitantes e o país B estará na ordem de {b:.0f} habitantes")