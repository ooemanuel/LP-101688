import os

os.system = ("cls || clear")

numero_um = int(input("digite o primeiro número: "))
numero_dois = int(input("digite o segundo número: "))

maior = max(numero_um, numero_dois)
menor = min(numero_um, numero_dois)

print(f"Numero 1: {numero_um}")
print(f"Numero 2: {numero_dois}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")