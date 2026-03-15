#02) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

print("Entre com login e senha")
print("Obs:.Apeas Texto. Login não pode ser igual a senha")

login = input("Login:  ")
senha = input("Senha:  ")

while login == senha:
  print("Erro!! Login igau a senha, tente novamente")
  login = input("Login:  ")
  senha = input("Senha:  ")
else:
  print("Logado")