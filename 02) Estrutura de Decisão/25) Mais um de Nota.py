#25) Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#	A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#	A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#	A mensagem "Aprovado com Distinção", se a média for igual a 10.


nome = input("Qual o nome do aluno? ")
sobrenome = input("Qual o sobrenome do aluno? ")
serie = input("Qual a série do aluno? ")
turma = input("Qual a turma do aluno? (A/B/C) ")
nota1 = float(input("Qual a nota do primeiro bimestre? "))
nota2 = float(input("Qual a nota do segundo bimestre? "))
nota3 = float(input("Qual a nota do terceiro bimestre? "))
media = (nota1 + nota2 + nota3) / 3

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
print("|  Segundo Bimestre: ", nota2, "                           |")
print("|  Terceiro Bimestre: ", nota3, "                           |")
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