import os


os.system("cls")  # Limpa o terminal

print("Solicitando dados.")

nome = input("\nDigite seu nome: ")

primeira_nota = float(input("\nDigite a primeira nota: "))
segunda_nota = float(input("\nDigite a segunda nota: "))
terceira_nota = float(input("\nDigite a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    print(f"\nSua média é {media} e você está aprovado")
else:
    print(f"\nSua média é {media} e você está reprovado")




                      
                      