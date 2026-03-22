# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

maior_acidente = -1
menor_acidente = 999999
cid_maior = cid_menor = 0
soma_veiculos = 0
soma_acid_menos_2000 = 0
cont_cid_menos_2000 = 0

for i in range(5):
    cod = int(input("\nCódigo da cidade: "))
    veiculos = int(input("Número de veículos de passeio: "))
    acidentes = int(input("Número de acidentes com vítimas: "))
    
    soma_veiculos += veiculos
    
    if acidentes > maior_acidente:
        maior_acidente = acidentes
        cid_maior = cod
        
    if acidentes < menor_acidente:
        menor_acidente = acidentes
        cid_menor = cod
        
    if veiculos < 2000:
        soma_acid_menos_2000 += acidentes
        cont_cid_menos_2000 += 1

print(f"\nMaior índice de acidentes: {maior_acidente} (Cidade {cid_maior})")
print(f"Menor índice de acidentes: {menor_acidente} (Cidade {cid_menor})")
print(f"Média de veículos nas 5 cidades: {soma_veiculos / 5:.2f}")

if cont_cid_menos_2000 > 0:
    media_menos_2000 = soma_acid_menos_2000 / cont_cid_menos_2000
    print(f"Média de acidentes em cidades com < 2000 veículos: {media_menos_2000:.2f}")
else:
    print("Nenhuma cidade possui menos de 2000 veículos.")