#11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#	a) o produto do dobro do primeiro com metade do segundo .
#	b) a soma do triplo do primeiro com o terceiro.
#	c) o terceiro elevado ao cubo.

inteiro1 = int(input("Digite um numero interio maior que 0: "))
inteiro2 = int(input("Digite um outro interio maior que 0: "))
real = float(input("Digite um numero real maior que 0: "))

if (inteiro1 > 0) and (inteiro2 > 0) and (real > 0):
  print((inteiro1 * 2) * (inteiro2 / 2)) #a
  print((inteiro1 * 3) + real) #b
  print(real**3)
else:
  print("Eu disse MAIOR QUE ZERO!!")