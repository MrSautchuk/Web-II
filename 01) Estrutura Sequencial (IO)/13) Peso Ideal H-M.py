#13) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#	Para homens: (72.7*h) - 58
#	Para mulheres: (62.1*h) - 44.7

genero = input("Qual seu genero? (H) para homem ou (M) para mulher ")
altura = float(input("Qual sua altura? "))

if (genero == "H") or (genero == "h"):
  print("Seu peso ideial de acordo com sua altura é: ", (72.7*altura) - 58)
elif (genero == "M") or (genero == "m"):
  print("Seu peso ideal de acordo com sua altura é: ", (62.1*altura) - 44.7)
else:
  print("Entrada incorreta!")