#18) Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print("Digite um numero de 1 a 7 para exibir o dia da semana correspondente")
print("(1)Domingo \n(2) Segunda-Feira \n(3) Terça-Feira \n(4) Qaurta-Feira \n(5) Quinta-Feira \n(6) Sexta-feira \n(7) Sabado")


num = int(input(":"))
dia = ""


if (num == 1):
  dia = "Domingo"
elif (num == 2):
  dia = "Segunda-Feira"
elif (num == 3):
  dia = "Terça-Feira"
elif (num == 4):
  dia = "Quarta-Feira"
elif (num == 5):
  dia = "Quinta-Feira"
elif (num == 6):
  dia = "Sexta-Feira"
elif (num == 7):
  dia = "Sabado"
else:
  print("Valor inserido incorreto")

if (dia == ""):
  print("Tente novamente")
else:
  print("O dia correspondente ao numero digitado foi: ", dia)