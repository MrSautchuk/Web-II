#17) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

#20) Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

loop = "s"

while loop == "s":
  print("O calculo de fatorial esta limitado a numeros inteiros maiores que 0 e menores que 16.")
  num = int(input("Fatorial de qual numero? "))
  if num > 0 and num < 16:
    i = num
    fat = num

    while i >= 2:
      fat = fat * (i - 1)
      i = i - 1

    print(f"O fatorial de {num} é {fat}")

    loop = input("Quer calcular o fatoial de outro numero? (s/n)").lower()
  else:
    print("Numero inserido fora do intervalo permitido.")
    break