#01) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


num = float(input("Entre com um numero entre 0 e 10 \n"))

while num > 10 and num < 0:
    num = float(input("Entre novamente com um numero entre 0 e 10 \n"))
    print("rodou")