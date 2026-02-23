#05) Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#06) A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#07) A mensagem "Reprovado", se a média for menor do que sete;
#08) A mensagem "Aprovado com Distinção", se a média for igual a dez.

nome = input("Qual o nome do aluno? ")
sobrenome = input("Qual o sobrenome do aluno? ")
serie = input("Qual a série do aluno? ")
turma = input("Qual a turma do aluno? (A/B/C) ")
nota1 = float(input("Qual a nota do primeiro semestre? "))
nota2 = float(input("Qual a nota do segundo semestre? "))
media = (nota1 + nota2) / 2

print("\n")
print("|====================================================|")
print("|                   Boletim escolar                  |")
print("|====================================================|")
print("|                                                    |")
print("|  Aluno: ", nome, sobrenome, "                           |")
print("|  Série: ", serie, " ano", turma, "                                 |")
print("|                                                    |")
print("|  Notas                                             |")
print("|  Primeiro Semestre: ", nota1, "                          |")
print("|  Segundo Semestre: ", nota2, "                           |")
print("|  A média final do aluno foi: ", media, "                 |")
print("|                                                    |")

if (media < 7):
  print("|  Aluno reprovado por ", 7 - media, " pontos abaixo da média  |")
elif (media >= 7) and (media < 10):
  print("|  Aluno aprovado                                    |")
elif (media == 10):
  print("|  Aluno aprovado om destinção!                      |")
else:
  print("|  Há alguma coisa errada com esta nota, por favor revise-a. |")
print("|====================================================|")
print("\n")
print("\n")