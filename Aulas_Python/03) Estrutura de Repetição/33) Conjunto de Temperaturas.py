# 33) O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que 
# leia as um conjunto indeterminado de temperaturas, e 
# informe ao final a menor e a maior temperaturas informadas, 
# bem como a média das temperaturas.

temperaturas = [10.1, 15.0, 3.0, 40.8, 50.0, 200.0, 30.5, 0.6, 350.1]
maior = temperaturas[0]
menor = temperaturas[0]

for i in range(len(temperaturas)):
  if menor > temperaturas[i]:
    menor = temperaturas[i]
  elif maior < temperaturas[i]:
    maior = temperaturas[i]

print(maior)
print(menor)