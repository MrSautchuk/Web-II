#13) Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("Em qual turno voce estuda?")
turno = input("Digite \n(M) Matutino\n(V) Vespertino\n(N) Noturno\n:")

if (turno == "M") or (turno == "m"):
  print("Bom dia!")
elif (turno == "V") or (turno == "v"):
  print("Boa tarde!")
elif (turno == "N") or (turno == "n"):
  print("Boa noite!")
else:
  print("você só pode entrar com os valores 'M', 'V' ou 'N' \nTente novamente.")