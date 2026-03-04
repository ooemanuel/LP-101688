import os

os.system("cls || clear")

print("""
================================== MENU =================================================
                        Código    Prato           Preço                                  
                        1         Picanha         R$ 25,00
                        2         Lasanha         R$ 20,00
                        3         Strogonoff      R$ 18,00
                        4         Bife Acebolado  R$ 15,00
                        5         Pão com ovo     R$ 5,00
======================================================================================= 
      """)

codigo = int(input("\nDigite o código do prato escolhido: "))

match codigo:
    case 1:
        print("\nPicanha | R$ 25,00")
    case 2:
        print("\nLasanha | R$ 20,00")
    case 3:
        print("\nStrogonoff | R$ 18,00")
    case 4: 
        print("\nBife Acebolado | R$ 15,00")
    case 5:
        print("\nPão com ovo | 5,00")
    case _:
        print("\nEscolha um dos códigos disponiveis")
        
print("\n================= AGRADECEMOS A PREFERÊNCIA =================") 