# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

nome_ginasta = input("Atleta: ")
notas = []

for i in range(7):
    nota = float(input("Nota: "))
    notas.append(nota)

melhor_nota = max(notas)
pior_nota = min(notas)

notas_validas = notas.copy()
notas_validas.remove(melhor_nota)
notas_validas.remove(pior_nota)
media_ginasta = sum(notas_validas) / 5

print("\nResultado final:")
print(f"Atleta: {nome_ginasta}")
print(f"Melhor nota: {melhor_nota}")
print(f"Pior nota: {pior_nota}")
print(f"Média: {media_ginasta:.2f}")