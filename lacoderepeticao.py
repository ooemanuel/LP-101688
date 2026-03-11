import os
import time

os.system("cls")


# #De 1 até 10
# for i in range(1, 11):
#     print(i)
#     #Espera dois segundos
#     time.sleep(2)
    
# #De 10 até 1    
# for i in range(10, -1, -1):
#     print(i)
#     #Espera dois segundos
#     time.sleep(1)
    
    
# #De 100 até 120 amostrando os números pares    
# for i in range(100, 121, 2):
#     print(i)
#     #Espera dois segundos
#     time.sleep(1)
    
    
n = int(input("Digite um número para fazer a contagem regressiva: "))

for i in range(n, 0, -1):
    print(i)
  
    time.sleep(1)  #Espera 1 segundo
    