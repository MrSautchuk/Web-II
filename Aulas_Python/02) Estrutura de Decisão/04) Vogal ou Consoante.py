#04) Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite apenas uma letra qualquer: ")

if (len(letra) == 1 and letra.isalpha()):
  if (letra == "a") or (letra == "e") or (letra == "i") or (letra == "o") or (letra == "u"):
    print("A letra digitada é uma vogal (", letra, ")")
  else:
    print("A letra digitada é um consoante (", letra, ")")
else:
  print("Você digitou mais de uma letra ou algum numero Mega-Mente!")
  print("Tenta de novo ¬¬")