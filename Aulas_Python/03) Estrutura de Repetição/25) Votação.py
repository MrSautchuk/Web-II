#25) Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

votosCandidato1 = 0
votosCandidato2 = 0
votosCandidato3 = 0

eleitores = int(input("Quantos eleitores vão votar? "))

while eleitores > 0:
  voto = int(input("Você votará em qual candidato? \n (1) Candidato 1 \n (2) Candidato 2 \n (3) Candidato 3 \n"))
  match voto:
    case 1:
      votosCandidato1 += 1
      print("Voto Computado")
    case 2:
      votosCandidato2 +=1
      print("Voto Computado")
    case 3:
      votosCandidato3+=1
      print("Voto Computado")
    case _:
      print("Voto inválido")
  eleitores -= 1


print(f"Votos do candidato 1 {votosCandidato1}")
print(f"Votos do candidato 2 {votosCandidato2}")
print(f"Votos do candidato 3 {votosCandidato3}")