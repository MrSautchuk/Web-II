#Atividade 1

nomes = ["maria","joao","jose","mané","silvio","silvia","ana","rafael","jonas","josefina"]
i = 0

while i < len(nomes):
    if i % 2 != 0:
        print (nomes[i])
    i += 1


#Atividade 2

numeros = [0,1,2,3,4,5,6,7,8,9]
quantidade = len(numeros)
soma = sum(numeros)
media = soma / len(numeros)

print(numeros)
print(f"dentro da lista tem {quantidade} numeros")
print(f"a soma entre todos os numeros é {soma}")
print(f"a media da soma dos valores é {media}")

#Atividade 3

frutas = ["jaca","mamão","banana","laranja","maçã"]
frutasOrdenas = sorted(set(frutas))
frutasReordenadas = sorted(frutas, reverse=True)

print(frutas)
print(frutasOrdenas)
print(frutasReordenadas)


#Atividade 4

data = input("Digite uma data no formato dd/mm/aaaa: ")
partes = data.split('/')
dia = partes[0]
mes = partes[1]
ano = partes[2]

print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")


nomes.pop(0)
print("Lista de nomes após remoção do primeiro elemento:", nomes)


numeros.pop(-1)
print("Lista de números após remoção do último elemento:", numeros)


meio = len(frutas) // 2
frutas.pop(meio)
print("Lista de frutas após remoção do elemento do meio:", frutas)


#Filtro de Busca

produtos = ['teclado', 'mouse', 'monitor']
busca = input("Digite o nome do produto que deseja buscar: ")

if busca in produtos:
    print(f"O produto '{busca}' está disponível na lista.")
else:
    print(f"O produto '{busca}' não foi encontrado na lista.")
