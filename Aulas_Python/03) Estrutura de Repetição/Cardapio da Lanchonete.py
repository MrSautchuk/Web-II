# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.


total_geral = 0

while True:
    codigo = int(input("Código do item (0 para encerrar): "))
    if codigo == 0:
        break
        
    qtd = int(input("Quantidade: "))
    preco = 0.0
    
    match codigo:
        case 100: preco = 1.20
        case 101: preco = 1.30
        case 102: preco = 1.50
        case 103: preco = 1.20
        case 104: preco = 1.30
        case 105: preco = 1.00
        case _:
            print("Código inválido!")
            continue
            
    total_item = preco * qtd
    total_geral += total_item
    print(f"Valor deste item: R$ {total_item:.2f}")

print(f"\nTotal Geral do Pedido: R$ {total_geral:.2f}")