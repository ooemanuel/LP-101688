Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/02/2026
Var
// Seção de Declarações das variáveis
   nome: caractere
   idade: inteiro
   
   primeira_nota: real
   segunda_nota: real
   soma: real
   media: real
   resultado: caractere


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   // Entrada de Dados
   escreval("Olá Aluno, seja bem-vindo!")
   escreval
   
   
   escreva("Digite seu nome: ")
   leia(nome)
   
   escreva("Digite sua idade: ")
   leia(idade)
   
   escreva("Digite a primeira nota: ")
   leia(primeira_nota)
   
   escreva("Digite a segunda nota: ")
   leia(segunda_nota)
   
   // PROCESSAMENTO
   
   soma <- primeira_nota + segunda_nota
   media <- soma / 2
   
   
   se media >= 7 entao
      resultado <- "Aprovado!"
   senao
      resultado <- "Reprovado!"
   fimse

   
   // SAIDDA
   escreval
   escreval(nome, idade, " anos")
   escreval("Sua nota 1 é: ", primeira_nota)
   escreval
   escreval("Sua nota 2 é: ", segunda_nota)
   escreval
   escreval("A médias das sua notas é: ", media)
   escreval
   escreval(nome, " você está ", resultado)

Fimalgoritmo