Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/02/2026
Var
   nota_primeira: real
   nota_segunda: real
   nota_terceira: real
   soma_das_notas: real
   media: real

Inicio
      escreva("Digite sua primeira nota: ")
      leia(nota_primeira)
      escreval
      
      escreva("Digite sua segunda nota: ")
      leia(nota_segunda)
      escreval
      
      escreva("Digte sua terceira nota: ")
      leia(nota_terceira)
      escreval
      
      soma_das_notas <- nota_primeira + nota_segunda + nota_terceira
      
      media <- soma_das_notas / 3
      
      se media >= 7 entao
         escreval("Sua média é: ", media, " e você está aprovado")
      senao
         escreval("Sua média é: ", media, " e você está reprovado")
      fimse


Fimalgoritmo