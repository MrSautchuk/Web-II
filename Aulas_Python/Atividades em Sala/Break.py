# Crie um programa que peça ao usuário para digitar 5
# números. Se o usuário digitar o número 0, o programa deve
# exibir "Processamento interrompido" e sair do laço usando
# break. Caso o usuário digite os 5 números sem inserir
# nenhum zero, o programa deve exibir "Sequência processada
# com sucesso" (usando a cláusula else).

for i in range(5):
    numero = int(input("Digite um numero: \n"))
    if numero == 0:
        break