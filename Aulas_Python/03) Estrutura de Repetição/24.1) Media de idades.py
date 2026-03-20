#24.1) Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

pessoas = []
idades = []
jovens = []
jovenNome = []
jovenQuantidade = 0
adultoNome= []
adultoQuantidade = 0
idosoNome = []
idosoQuantidade = 0
soma = 0
quantidade  = int(input("Quantas pessoas tem na sala? "))

for i in range(quantidade):
  pessoa = input(f"Qual o nome da {i +1}º pessoa? ")
  idade = int(input("Quantos anos ela tem? "))
  soma += idade
  pessoas.append(pessoa)
  idades.append(idade)

# print(idades[0])
# print(idades[1])
# print(idades[2])
# print(idades[3])
# print(pessoas[0])
# print(pessoas[1])
# print(pessoas[2])
# print(pessoas[3])

i = quantidade

while i > 0:
  i -= 1
  loop = idades[i]
  if loop >= 60:
    idosoNome.append(pessoas[i])
    idosoQuantidade += 1
  elif loop < 60 and loop >= 25:
    adultoNome.append(pessoas[i])
    adultoQuantidade += 1
  elif loop < 25 and loop > 0:
    jovenNome.append(pessoas[i])
    jovenQuantidade += 1


print(f"Existem {idosoQuantidade} idosos na sala sendo eles : {idosoNome}")
print(f"Existem {adultoQuantidade} adultos na sala sendo eles : {adultoNome}")
print(f"Existem {jovenQuantidade} jovens na sala sendo eles : {jovenNome}")
print(f"A soma da idade de todas as pessoas na sala é {soma}")
print(f"A media das idades das pessoas na sala é {(soma / quantidade):.2f}")