import os

os.system("cls || clear")

login_cadastrado = "emanuel.chagas"

senha_cadastrada = "03012007"

login = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if senha == senha_cadastrada and login == login_cadastrado:
    print("Seja bem vindo!")
else: 
    print("Login ou senha inválidos!")
