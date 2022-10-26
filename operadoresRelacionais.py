#OPERADORES DE COMPARAÇÃO

# == (igual a)
# != (diferente de)
# >>= (maior ou igual a)
# <= (Menor ou igual a)
# > (maior que)
# < (menor que)



#OPERADORES LOGICOS AND E  OR

"""
10 > 18 and 3 > 2
#false

20 > 18 or 3>4
#verdadeiro

1 > 2 and 2 > 3 or 1 > 0
#verdadeiro: pois a ordem de priorização é > or, not e and. Desse modo, a parte a esquerda de or passou a ser sua esquerda e a direita sua direita. 

numero = 10
print (numero>0 and numero<10)
print (numero>0 or numero<10)
"""


#DESVIO CONDICIONAL
cupom = input("Digite seu cupom: ")

#fuctura é o cupom valido que o usuario tem de ter inserido, um desses dois.
if( cupom == "fuctura1" or cupom == "fuctura2"):
    print ("você ganhou 15% de desconto!")
else:
    print ("Cupom inserido inválido!")