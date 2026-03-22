# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

gabarito = []
print("--- Professor, digite o gabarito ---")
for i in range(10):
    gabarito.append(input(f"Questão {i+1}: ").upper())

maior_acerto = -1
menor_acerto = 11
total_alunos = 0
soma_notas = 0

while True:
    print("\n--- Vez do Aluno ---")
    nota_aluno = 0
    for i in range(10):
        resp = input(f"Resposta da questão {i+1}: ").upper()
        if resp == gabarito[i]:
            nota_aluno += 1
            
    total_alunos += 1
    soma_notas += nota_aluno
    
    if nota_aluno > maior_acerto: maior_acerto = nota_aluno
    if nota_aluno < menor_acerto: menor_acerto = nota_aluno
        
    continuar = input("Outro aluno vai utilizar? (S/N): ").upper()
    if continuar == 'N':
        break

print("\n--- Estatísticas da Turma ---")
print(f"Maior acerto: {maior_acerto}")
print(f"Menor acerto: {menor_acerto}")
print(f"Total de alunos: {total_alunos}")
if total_alunos > 0:
    print(f"Média da turma: {soma_notas / total_alunos:.1f}")