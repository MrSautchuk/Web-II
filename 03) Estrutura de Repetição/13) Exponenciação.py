#13) Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = float(input("Digite o numero a ser usado como base: "))
expoente = float(input("igite o numero a ser usado como expoente: "))
i = expoente

while i > 0:
  print(f"{base} X {expoente} = {base * expoente}")
  base = base * expoente
  i -= 1

print(f"Realizando o calculo de elevação chegamos ao resultado {base}")