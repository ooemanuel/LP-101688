import os

os.system("cls || clear")

nome_aluno = input("Digite seu nome: ")
nota_um = float(input("Digite a sua primeira nota: "))
nota_dois = float(input("Digite a sua segunda nota: "))

media = (nota_um + nota_dois) / 2

if media >= 9:
    print(f"\nNome: {nome_aluno}")
    print(f"\nSua média é: {media}")
    print("\nSeu conceito é: A")
    print("\nAprovado (A)")
elif media >= 7.5:
    print(f"\nNome: {nome_aluno}")
    print(f"\nSua média é: {media}")
    print("\nSeu conceito é: B")
    print("\nAprovado (A)")
elif media >= 6:
    print(f"\nNome: {nome_aluno}")
    print(f"\nSua média é: {media}")
    print("\nSeu conceito é: C")
    print("\nAprovado (A)")
elif media >= 4:
    print(f"\nNome: {nome_aluno}")
    print(f"\nSua média é: {media}")
    print("\nSeu conceito é: D")
    print("\nReprovado (A)")
else:
    print(f"\nNome: {nome_aluno}")
    print(f"\nSua média é: {media}")
    print("\nSeu conceito é: E")
    print("\nReprovado (A)")