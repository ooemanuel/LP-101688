import os

os.system = ("cls || clear")

numero_um = int(input("digite o primeiro número: "))
numero_dois = int(input("digite o segundo número: "))
numero_tres = int(input("Digite o terceiro número: "))

maior = max(numero_um, numero_dois, numero_tres)
menor = min(numero_um, numero_dois, numero_tres)




print(f"Numero 1: {numero_um}")
print(f"Numero 2: {numero_dois}")
print(f"Numero 3: {numero_tres}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")