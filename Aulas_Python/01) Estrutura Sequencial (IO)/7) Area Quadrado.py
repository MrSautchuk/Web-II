#07) Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lados = int(input("Quantos CM tem os lados do quadrado? "))
area = lados * lados
dobro = area * 2

print("Se os lados do quadrado tem ", lados, "centimetros")
print("então a area do quadrado é: ", area)
print("e o dobro desta area é de: ", dobro)