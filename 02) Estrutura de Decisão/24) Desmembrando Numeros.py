#24) Faça um Programa que leia um número inteiro menor que 1000 
# e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#	Observando os termos no plural a colocação do "e", da vírgula entre outros. 
# Exemplo:
#	326 = 3 centenas, 2 dezenas e 6 unidades
#	12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input("Digite um numeoro inteiro menor que 1000:\n"))
centenas = num // 100
dezenas = (num % 100) // 10
unidades = num % 10

print(f"{int(centenas)} centenas, {int(dezenas)} dezenas e {int(unidades)} unidades")

