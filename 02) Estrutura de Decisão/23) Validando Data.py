#23) Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

from datetime import datetime


data = input("digite uma data no formato dd/mm/aaaa:\n")


def validar_data(data):
  try:
    datetime.strptime(data, '%d/%m/%Y')
    return True
  except ValueError:
    return False

print(validar_data(data))