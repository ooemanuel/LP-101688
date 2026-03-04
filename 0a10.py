import os

os.system("cls || clear")

nota = float(input("Digite uma nota (0 a 10): "))

if nota >= 0 and nota <= 10:
    print(f"A nota digitada foi: {nota}")
else:
    print("A nota informada deve ser entre 0 e 10")