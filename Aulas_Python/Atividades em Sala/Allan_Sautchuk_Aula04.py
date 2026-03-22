# Exercicio 1
numero = int(input("Digite um número inteiro: "))
match numero:
    case -1:
        print("Saíndo do sistema")
    case _:
        print("Ok vamos lá")

# Exercicio 2
nota = float(input("\nDigite a nota do aluno: "))
if nota > 7:
    print("Aprovado")
elif nota > 4:
    print("Recuperação")
else:
    print("Reprovado")

# Exercicio 3
nome = input("\nDigite o nome de uma pessoa: ").strip()
match len(nome) % 2:
    case 0:
        print("O número de caracteres é par.")
    case 1:
        print("O número de caracteres é ímpar.")

# Exercicio 4
num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num2 == 0:
    print("Erro: Divisão por zero.")
else:
    resto = num1 % num2
    if resto == 0:
        pass
    elif resto % 2 == 0:
        print(f"Resto par. Multiplicação: {num1 * num2}")
    else:
        print(f"Resto ímpar. Soma: {num1 + num2}")

# Exercicio 5
previsao = input("\nQual a previsão do tempo (chuva, sol, nublado)? ").strip().lower()
match previsao:
    case "chuva":
        print("use guarda chuvas")
    case "sol":
        print("não esqueça o filtro solar")
    case "nublado":
        print("O tempo está ótimo")
    case _:
        print("opção inválida")