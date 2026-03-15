#30) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#	-"Telefonou para a vítima?"
#	-"Esteve no local do crime?"
#	-"Mora perto da vítima?"
#	-"Devia para a vítima?"
#	-"Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Esta é a investigação de um assassinato.")
print("Como você foi um dos ultimos a ver a vítima viva, preciso que responda algumas perguntas.")
print("Responda apenas (s) para sim e (n) para não.")
p1 = input("Telefonou para a vítima? ").lower() == "s"
p2 = input("Esteve no local do crime? ").lower() == "s"
p3 = input("Mora perto da vítima? ").lower() == "s"
p4 = input("Devia para a vítima? ").lower() == "s"
p5 = input("Já trabalhou com a vítima? ").lower() == "s"
print("\n")
print("Critério de avaliação")
print("2 respostas positivas......(Suspeito)")
print("3~4 respostas positivas....(Cúmplice)")
print("5 resposta positivas.......(ASSASSINO)")
respostas = [p1, p2, p3, p4, p5]
print("\n")
print(respostas)
print("\n")

if (sum(respostas) == 5):
  print("ASSASSINO!! Está preso!!")
elif (sum(respostas) == 4):
  print("Cúmplice")
elif (sum(respostas) == 3):
  print("Cúmplice")
elif (sum(respostas) == 2):
  print("Suspeito")
elif (sum(respostas) == 1):
  print("Inocente")
elif (sum(respostas) == 0):
  print("Inocente")