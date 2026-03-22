# 38) Uma academia deseja fazer um senso entre seus clientes para descobrir 
# o mais alto, 
# o mais baixo, 
# a mais gordo 
# e o mais magro, 
# para isto você deve fazer um programa que pergunte a cada um dos clientes da academia 
# seu código, 
# sua altura e 
# seu peso. 
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
# Ao encerrar o programa também deve ser informados 
# os códigos e valores do clente mais alto, 
# do mais baixo, 
# do mais gordo e 
# do mais magro, 
# além da média das alturas e 
# dos pesos dos clientes

alto = [0, 0, 0]
baixo = [999, 999, 999]
gordo = [0, 0, 0]
magro = [999, 999, 999]
alturas = []
pesos = []

while True:
  cod = int(input("Codigo do cliente: "))
  if cod == 0:
    break
  altura = float(input("Altura do cliente: "))
  alturas.append(altura)
  peso = float(input("Peso do cliente: "))
  pesos.append(peso)

  if baixo[1] > altura:
    baixo[0] = cod
    baixo[1] = altura
    baixo[2] = peso

  if alto[1] < altura:
    alto[0] = cod
    alto[1] = altura
    alto[2] = peso

  if magro[2] > peso:
    magro[0] = cod
    magro[1] = altura
    magro[2] = peso

  if gordo[2] < peso:
    gordo[0] = cod
    gordo[1] = altura
    gordo[2] = peso


print(f"O mais alto cliente {alto[0]}, {alto}")
print(f"O mais baixo cliente {baixo[0]}, {baixo}")
print(f"O mais gordo cliente {gordo[0]}, {gordo}")
print(f"O mais magro cliente {magro[0]}, {magro}")
print(f"A soma de todas as alturas é: {sum(alturas)}")
print(f"Asoma de todos os pesos é: {sum(pesos)}")