# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.


c1 = c2 = c3 = c4 = nulos = brancos = total_votos = 0

print("1-José | 2-João | 3-Maria | 4-Ana | 5-Nulo | 6-Branco | 0-Encerrar")

while True:
    voto = int(input("Digite o voto: "))
    if voto == 0:
        break
        
    match voto:
        case 1: c1 += 1
        case 2: c2 += 1
        case 3: c3 += 1
        case 4: c4 += 1
        case 5: nulos += 1
        case 6: brancos += 1
        case _: 
            print("Voto inválido")
            continue
            
    total_votos += 1

print("\n--- Resultado ---")
print(f"José: {c1} | João: {c2} | Maria: {c3} | Ana: {c4}")
print(f"Nulos: {nulos} | Brancos: {brancos}")

if total_votos > 0:
    print(f"% Nulos: {(nulos/total_votos)*100:.2f}%")
    print(f"% Brancos: {(brancos/total_votos)*100:.2f}%")