Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/02/2026
Var
   SALARIO_MINIMO: real
   salario_empregador: real
   salario_equivalente: real
Inicio
      SALARIO_MINIMO <- 1621
      
      escreva("Digite o valor do seu salario: ")
      leia(salario_empregador)
      
      escreval

      salario_equivalente <- salario_empregador / SALARIO_MINIMO

      escreval("Você ganha: R$", salario_empregador, )
      escreval
      escreval("Esse valor equivale a ", salario_equivalente:3:1, " salários minimos")
      


Fimalgoritmo