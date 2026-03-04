import os

os.system("cls")

numero_um = int(input("\nDigite um número: "))
numero_dois = int(input("\nDigite um número: "))

caractere = input("\nEscolha uma operação (+ , -, /, *): ")

match caractere:
    case "+":
        soma = numero_um + numero_dois
        print(f"\nA soma é: {soma}")
    case "-":
        menos = numero_um - numero_dois
        print(f"\nA subtração é: {menos}")
    case "/":
        dividir = numero_um / numero_dois
        print(f"\nA divisão é: {dividir}")
    case "*":
        multiplicacao = numero_um * numero_dois
        print(f"\nA multiplicação é: {multiplicacao}")
    case _:
        print("\nOperação invalida! Escolha uma das opções disponiveis! ")

print("\n===FIM===")
         
    