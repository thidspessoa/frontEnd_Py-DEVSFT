#OPERADORES ARITIMETICOS 

#exponenciação = **
"""Quando elevamos um numero a ele mesmo, isso siginifica que vai multiplicar o numero por ele mesmo a quantidade de vezes
que ele representa.
Ex: 2²=4"""

#Divisão inteira = //
"""O valor da divisão de dois numeros mas so retorna o valor inteiro desse resultado."""

#Resto da divisão = %
"""Diferente da divisão inteira, retorna somente o resto da divisão, o valor que resta apos os dois numeros serem divididos
Ex: 11%5=1.
"""
"""Podemos usar para uma logica que descubra se um numero é par, 
EX:
x%2 == 0 -> par caso o resto da divisão por dois seja 0
print(X)"""


#DECLARAR VARIAVEL

#A importância de uma variavel é para a manipulação de dados no código.
"""Variaveis em python não aceitam letras maiuculas no inicio, caracteres especiais
que não estejam em cima da letra e operadores aritimeticos."""

"""Não utilizar mais que 3 palavras ou acentos em letras, é recomendado
como boa pratica."""

"""Você precisa antes de utilizar uma variavel, declara-la."""

#x -= 1
"""É possivel abreviar operações aritimeticas dentro de variaveis. 
EX: x-=1 seria o equivalente a x-1. Operando o x pelo valor apos o sinal de igual. """

#Teste
print ((18 // 4), (18 % 4), (18/4))

##

n = input ("Pois sou: ") #usuario entra com valor inteiro
#vai ser uma string pois todo dado recebido por input é por padrão string.
print (type(n))
