import os

os.system("cls || clear")

peso = float(input("\nInsira seu pego (em KG): "))
altura = float(input("\nInsira sua altura: "))

peso_vezes_peso = altura * altura
imc = peso / peso_vezes_peso


if imc >= 40:
    print(f"\nSeu imc é {imc:.1f}")
    print("\nObesidade III (mórbida)")
elif imc >= 35:
    print(f"\nSeu imc é {imc:.1f}")
    print("\nObesidade II (severa)") 
elif imc >= 30:
    print(f"\nSeu imc é {imc:.1f}")
    print("\nObesidade I")
elif imc >= 25:
    print(f"\nSeu imc é {imc:.1f}")
    print("\nLevemente acima do peso")
elif imc >= 18.6:
    print(f"\nSeu imc é {imc:.1f}")
    print("\nPeso ideal! Parabéns! Continue assim!")
else:
    print(f"\nSeu imc é {imc:.1f}")
    print("\nAbaixo do peso")
    