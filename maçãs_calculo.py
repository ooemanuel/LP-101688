import os

os.system("cls || clear")

print("---BEM VINDO A LOJA DE MAÇÃS---")
print("\nCaso desejar menos de 12 maçãs, o preço por unidade será R$ 1,30")
print("\nCaso desejar mais de 12 maçãs, o preço por unidade será R$ 1,00")

quantidade = int(input("\nDigite a quantidade desejadas de maçãs: "))

if quantidade >= 12:
    valor_maca =  quantidade * 1.00
    print("\nO valor por maçã é R$ 1,00")
    print(f"\n--O total é: R$ {valor_maca}--")
else:
    valor_maca = quantidade * 1.30
    print("\n*O valor por maçã é R$ 1,30*")
    print(f"\n--O total é: R$ {valor_maca:.2f}--")
    
print("Agradecemos a preferência! Volte sempre!")
    

