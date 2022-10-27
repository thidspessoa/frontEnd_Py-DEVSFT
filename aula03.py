"""
cupom1 = "SENAC1"
cupom2 = "SENAC2"
cupom = input("Digite o cupom: ")

if ((cupom == cupom1) or (cupom == cupom2)):
    print ("Você ganhou 15% de desconto!")
else:
    print ("Cupom inserido inválido. \n")
    print ("Cortesia de 10% de desconto aplicado!")
"""


## DESCONTOS: 15%, 10%, 5%
"""
cupom1 = "FUCTURA1"
cupom2 = "FUCTURA2"
cupom = input("Digite o cupom: ")
"""
"""A ordem obrigatoria a ser seguida é usar o elif abaixo do if, seguindo a logia
que caso se a condição um seja falsa, tente isso no elif e caso todas as condições anteriores
sejam falsas, utilize a condição final else.
   Porem o else não é obrigatorio ser inserido, o codigo pode terminar sem o else.
   Também é possivel utilizar if dentro de outros ifs. """
"""
if (cupom == cupom1):
    print ("Você ganhou 15% de desconto!")
elif (cupom == cupom2):
    print ("Você ganhou 10% de desconto!")
else:
    print ("Cortesia de 5% de desconto aplicado.")
"""


##TIPOS DE PRINT
var1 = 18.00
var2 = "João"

#.format
print(f"Olá eu sou {var2}", f"e tenho {18} anos de idade", "\n")
#.format com string
print("Olá eu sou o {}".format(var2), "\n")


#com % (Neste metodo na referencia você precisa dizer o tipo da variavel com a primeira letra do tipo)
print("Meu nome é %s e tenho %d anos de idade" %(var2, var1), "\n")
print("")

""" 
%s -> String
%d -> inteiros
%.2f -> reais
%.2e -> exponencial 

Nos dois ultimos metodos, o numero dois seria equivalente ao numero de casas decimais
que você deseja que apareça apos a virgula.
"""


##QUEBRA DE LINHA
#qubra de linha com \n


#ORDEM DE SEPARAÇÃO

"""Operador logico, operadores de comparação. """