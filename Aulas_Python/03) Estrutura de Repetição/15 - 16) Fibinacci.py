#15) A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

#16) A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

p = 0
s = 1
sequencia = p + s
print(sequencia)
n = int(input("Quer ver a serie até qual termo? "))

while sequencia <= n:
  if sequencia <= 700:
    print(sequencia, ",", end=" ")
    p = s
    s = sequencia
    sequencia = p + s
  else:
    break