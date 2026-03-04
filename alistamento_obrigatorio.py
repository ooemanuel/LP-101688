import os

os.system("cls || clear")

sexo = input("Digite seu gênero (M OU F): ").lower()
ano_nascimento = int(input("Digite o ano que você nasceu (XXX): "))

apto = 2026 - ano_nascimento

sexo_apto = sexo == "m"


if sexo_apto and apto >= 18:
    print("\nDeve-se apresentar para o serviço militar obrigatório")
else:
    print("\nVocê não está apto para o serviço militar obrigatório")