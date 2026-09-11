Algoritmo "Calculo_Municao"

Var
   quantidade, preco, resultado1, cpfscancelados, minimo_balas: real
   enter : caractere

Inicio
   escreval("Sou um ajudante/calculadora da sua compra de munições de 38.")
   escreval("Para prosseguir aperte enter:")
   leia(enter)

   escreval("Quantas munições de 38 você quer comprar? ")
   leia(quantidade)
   escreval("Qual o preço de cada uma? ")
   leia(preco)

   resultado1 <- quantidade * preco

   escreval("Quantos pretende eliminar? ")
   leia(cpfscancelados)

   minimo_balas <- quantidade / cpfscancelados

   se (quantidade >= cpfscancelados) entao
      escreval("Espero que seja bom de pontaria, pois você tem ", minimo_balas, " balas por cabeça!")
      escreval("Sua compra ficou ", resultado1)
   senao
      escreval("Você precisa de mais balas!")
   fimse

Fimalgoritmo