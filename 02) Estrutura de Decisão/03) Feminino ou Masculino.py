#03) Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = input("Qual seu genero? F/M ")

if (genero == "F") or (genero == "f"):
  print("seu genero é: Feminino (",genero,")")
elif (genero == "M") or (genero == "m"):
  print("seu genero é: Masculino (",genero,")")
else:
  print("Genero não expecificado, tente novamente. (",genero,")???")