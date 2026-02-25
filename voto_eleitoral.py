import os

os.system("cls || clear")


# nome = input("Digite seu nome:  ")

idade = int(input("Digite sua idade: "))


if idade < 16:
    print("Não pode votar.")
elif 16 <= idade < 18:
    print("Voto opcional.")
elif 18 <= idade <= 65:
    print("Voto obrigatório.")
else:
    print("Voto opcional (não é obrigado a votar).")
    
    