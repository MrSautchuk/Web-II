#Crie uma lista que armazene 10 nomes de pessoas e depois exiba na tela somente os nomes cujos indices sejam impares.

nomes = []
i = 0

while i < 10:
  nome = input("Digite um nome para adicionar à lista: ")
  nomes.append(nome)
  i += 1

print(nomes)



#Crie uma lista para armazenar 10 números e depois exiba:
#Quantos números foram armazenados, 
#O calculo da soma de todos os números e 
#A média de todos os números.

numeros = [1,2,3,4,5,6,7,8,9,10]
i = 0
soma = 0

print(len(numeros))

while i in range(10):
  soma += numeros[i]
  i += 1

print(soma)
print(soma / len(numeros))


#Crie uma lista com 5 frutas e depois exibe em ordem alfabética crescente e decrescente.

frutas = ["Maçã", "Banana", "Uva", "Abacaxi", "Laranja"]
print(f"A sequencia digitada foi: {frutas}")

frutas.sort()
print(f"Em ordem alfabetica fica: {frutas}")

frutas.sort(reverse=True)
print(f"De tras para a frente: {frutas}")


#Peça uma data ao usuário no formato “dd/mm/aaaa” usando o método split exiba na tela Dia: dd, Mês: 
#mm e Ano: aaaa

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")

print(f"Dia: {dia}, Mês: {mes} e Ano: {ano}")


#5) Remova o primeiro elemento da lista do exercício 1, o último da segunda lista e o elemento do meio da terceira lista. Depios exiba na tela.

nomes[0].remove

#6) Filtro de Busca (Contexto Web): "Dada uma lista de nomes de produtos ['Teclado', 'Mouse', 'Monitor'], crie um programa que receba uma string de busca do usuário e verifique se o item está na lista (usando o operador in)."