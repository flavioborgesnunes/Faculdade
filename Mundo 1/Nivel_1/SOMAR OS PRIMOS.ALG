Algoritmo "Somar os primos"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/05/2022
Var
// Seção de Declarações das variáveis 
   num, contUm, contDois, eZero, soma:inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Digite um Número:")
leia(num)
para contUm  de 1 ate num faca
     eZero <- 0
     para contDois de 1 ate contUm faca
          se(contUm mod contDois = 0) entao
                    eZero<- eZero + 1
          fimse
     fimpara
     se (eZero = 2) entao
     escreval("O número", contUm, " é primo")
     soma <- (soma + contUm)
     fimse
fimpara
escreva("A soma de todos os números menores iguais a ", num, " é ", soma)

Fimalgoritmo