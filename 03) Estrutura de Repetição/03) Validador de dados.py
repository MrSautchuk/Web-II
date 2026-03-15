#03) Faça um programa que leia e valide as seguintes informações:
#	-Nome: maior que 3 caracteres;
#	-Idade: entre 0 e 150;
#	-Salário: maior que zero;
#	-Sexo: 'f' ou 'm';
#	-Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu nome (maior que tres caracteres): ")
while len(nome) <= 3:
	nome = input("Nome inválido. Digite um nome com mais de 3 caracteres: ")

idade = int(input("Digite sua idade (entre 0 e 150): "))
while idade < 0 or idade > 150:
	idade = int(input("Idade inválida. entre 0 e 150: "))

salario = float(input("Digite seu salário (maior que 0): "))
while salario < 0:
	salario = float(input("Salário invalido, digite o salário maior que 0: "))

sexo = input("Digite sua orientação sexual (f/m): ").lower()
match sexo:
	case "f":
		print("Quase finalizando")
	case "m":
		print("Quase finalizando")
	case _:
		sexo = input("Dados invalidos. Digite sua orientação sexual (f/m): ")

estadoCivil = input("Digite para estado civil: \n (s) para Solteiro \n (c) para Casado \n (v) para Viuvo \n (d) para Divorciado: ")
match estadoCivil:
	case "s":
		print("Dados validados.")
	case "c":
		print("Dados validados.")
	case "v":
		print("Dados validados.")
	case "d":
		print("Dados validados.")
	case _:
		estadoCivil = input("Estado civil invalido. (s) para Solteiro \n (c) para Casado \n (v) para Viuvo \n (d) para Divorciado: ")
		
print(f"Nome : {nome}")
print(f"Idade : {idade}")
print(f"Salario : R${salario}")
print(f"Orientação sexual : {sexo}")
print(f"Estado Civil : {estadoCivil}")