import os 

os.system ("cls || clear")

nome_empregado = input("\nDigite seu nome: ")

matricula_empregado = int(input("\nInforme sua matrícula: "))

ano_nascimento_empregado = int(input("\nInforme o ano do seu nascimento (4 Dígitos (XXX)):  "))

tempo_de_trabalho_empregado = int(input("\nInforme a quantidade de anos trabalhado (2 Digitos):  "))

idade_empregado = 2026 - ano_nascimento_empregado

if idade_empregado >= 65 or tempo_de_trabalho_empregado >= 30:
    situação_aponsentadoria = ("\nRequerer aposentadoria")
else:
     situação_aponsentadoria = ("\nNão requerer aposentadoria")

print(f"\nNome: {nome_empregado}")
print(f"\nMatricula: {matricula_empregado}")
print(f"\nSituação da sua aposentadoria: {situação_aponsentadoria}")