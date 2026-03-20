contador: int = 1
soma:int = -1000

if contador <= 1000:
    soma = soma + contador
    contador = contador + 1 
else:
    print("O total é: " + soma)