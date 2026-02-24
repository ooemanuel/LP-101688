import os

os.system("cls || clear")

idade = int(input("Digite sua idade: "))


if idade < 18:
    print("Acesso Negado")
else:
    print("Acesso permitido.")
    
print("Programa encerrado")