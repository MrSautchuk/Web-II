#22) Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("De que ano estamos falando?\n"))

if ((ano % 4) == 0) and ((ano % 100) == 0):
    print(ano, "é um ano bissexto")
else:
  print("Não é bisexto")