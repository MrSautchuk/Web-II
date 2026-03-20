#21) Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#	-Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#	-Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#	-Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


print("Você precisa resolver uma equação de segundo grau?")
print("informe os coeficientes nas posições 'a', 'b' e 'c' da formula ax^2 + bx + c=0")
a = float(input("informe o valor de a: "))

if (a == 0):
  print("Isso não é uma equação de segundo grau")
else:
  b = float(input("informe o valor de b: "))
  c = float(input("informe o valor de c: "))
  delta = b**2 - 4*a*c
  x1 = ((-b)+delta**0.5)/(2*a)
  x2 = ((-b)-delta**0.5)/(2*a)


if (delta < 0):
  print("O valor de DELTA é negativo, portanto não existe raiz real")
elif (delta == 0):
  print(x1)
else:
  print(x1)
  print(x2)