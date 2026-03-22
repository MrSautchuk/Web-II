# 40) Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.


maior_altura = 0
menor_altura = 999
id_maior = 0
id_menor = 0

for i in range(10):
    aluno_id = int(input(f"Digite o número do {i+1}º aluno: "))
    altura = int(input(f"Digite a altura do {i+1}º aluno (em cm): "))

    if altura > maior_altura:
        maior_altura = altura
        id_maior = aluno_id
        
    if altura < menor_altura:
        menor_altura = altura
        id_menor = aluno_id

print(f"Aluno mais alto: Nº {id_maior} com {maior_altura}cm")
print(f"Aluno mais baixo: Nº {id_menor} com {menor_altura}cm")