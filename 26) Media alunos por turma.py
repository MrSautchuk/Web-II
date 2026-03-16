#26) Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input("quantas turmas tem nesta escola? "))
print("Entre com a quantidade de alunos por turma, lembrando que cada turma não pode conter mais que 40 alunos.")
totalAlunos = 0
loop = turmas

while loop > 0:
  i = 1
  alunos = int(input("Quantos aluos tem na {i}º turma? "))
  totalAlunos += alunos
  loop -= 1

print(f"O total de alunos nesta escola é: {totalAlunos}")
print(f"A media de alunos por sala é: {totalAlunos / turmas}")