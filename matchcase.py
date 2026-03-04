import os

os.system("cls || clear")

dia = input("Digite o dia da semana: ").lower()

match dia:
    case "segunda":
        print("\nHoje é segunda-feira.")
    case "terça":
        print("\nHoje é terça-feira")
    case "quarta":
        print("\nHoje é quarta-feira")
    case "quinta":
        print("\nHoje é quinta-feira")
    case "sexta":
        print("\nHoje é sexta-feira!")
    case "sabado" | "domingo":
        print("\nHoje é fim de semana!")
    case _:
        print("\nDia inválido")
    
print(dia)

print("\n===FIM===")