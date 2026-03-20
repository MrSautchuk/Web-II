frase = input("Digite uma frase curta \n")
letra = input("Digite uma letra qualquer \n")
loop = 0
i = 0
quantidade = len(frase)
caractere = frase[loop]

while loop < quantidade:
    caractere = frase[loop]
    if (caractere == letra):
        i +=1
    loop += 1

print("A letra selecionada foi encontrada ", i, " vezes")