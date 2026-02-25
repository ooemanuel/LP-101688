import os

os.system("cls || clear")

numero_primeiro = int(input("Digite um número: "))

numero_segundo = int(input("Digite um segundo número: "))


soma = numero_primeiro + numero_segundo

media = soma / 2 

produto = numero_primeiro * numero_segundo

if numero_primeiro > numero_segundo:
    menor = numero_segundo
    maior = numero_primeiro
else:
    menor = numero_primeiro
    maior = numero_segundo
 
  
print(f"\nA média entre os números é {media}")
print(f"\nA soma entre os números é {soma}")
print(f"\nO produto entre os números é {produto}")
print(f"\nO número maior é {maior}")
print(f"\nO número menor é {menor}")


if numero_primeiro == numero_segundo:
    valor_igual = print("\nOs valores informados são iguais")
else: 
    valor_diferente = print("\nOs valores são diferentes")


