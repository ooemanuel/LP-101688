import os

os.system("cls")

print("--------------SEJA BEM VINDO--------------")

media = float(input("\nDigite sua média: "))
numero_de_faltas = int(input("\nDigite sua quantidade de faltas: "))

if media >= 7 and numero_de_faltas <= 40:
    print("\nParabéns! Aprovado!")
else:
    print("\nQue pena! Reprovado!")