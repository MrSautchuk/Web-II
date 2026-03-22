# 29) O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

# 30) Preço do pão: R$ 0.18
# 	Panificadora Pão de Ontem - Tabela de preços
# 	1 - R$ 0.18
# 	2 - R$ 0.36
# 	...
# 	50 - R$ 9.00

print("Panificadora Pão de Ontem - Tabela de preços")

for i in range(51):
  if i == 0:
    print(" ")
  else:
    if i < 10:
      print(f"0{i}  -  R$ {i * 0.18:.2f}")
      i += 1
    else:
      print(f"{i}  -  R$ {i * 0.18:.2f}")
      i += 1