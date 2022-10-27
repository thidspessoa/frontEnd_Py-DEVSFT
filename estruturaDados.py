##Estruturas de dados armazenam mais de um valor.

##LISTAS
"""Lista vazia"""
lista1 = []
print (lista1)

"""Declaração explicita de lista"""
lista2 = list(lista2(1,"dd",30.00))


"""Declaração implicita"""



"""Para chamar uma lista você chama a sua indexão que inicia apartir de 0,
chamando os elementos que você deseja imprimir com suas respectivas posições.
Também é possivel imprimi elementos de uma lista dentro de outra lista, ou uma
lista dentro de uma lista dentro de outra lista, e caso você coloque para acessar
outra posição apos inserir a posição de um sublista dentro de outra, ela irá
imprimir a letra correspondente a posição caso o dado naquela posição seja uma
string ou uma lista (caminhar entre as posições). EX:

print(lista1[1][2][9])"""



"""Você pode inserir uma lista dentro de outra lista."""


#FATIAR LISTA
#nomeDaLista[start:stop:step]
print(lista2[2:6:2])
"""O stop significa que não irá até o 6 exatamente, mas sim se pensa 5-1, ou seja
ele irá ate o 5 elemento desta lista.
   O start diz de qual elemento se iniciar
   O step diz de quanto em quanto se deve imprimir um elemento, no exemplo acima
   são de duas em duas casas."""

print(lista3[-1])
"""Quando usamos -1 queremos imprimir o ultimo elemento."""

print (lista3[1:])
"""Quando não declaramos um stop e um step, queremos imprimir todos os elementos."""

print(lista3[::])
"""Imprime a lista toda"""


print (len(lista2[3]))
"""O metodo len diz quantas letras e caracteres tem um elemento."""



#adicionar a lista

lista1.append("python")
print(lista1)
"""O metodo append so aceita um argumento por vez."""

lista1.insert(2, "c++")
print (lista1)
"""Metodo insert permite adicionar elementos em uma posição especifica."""


#remover elemento

lista1.remove("Java")
print(lista1)
"""Remove o elemento usando o nome do elemento como parametro."""

#Copiar lista

a = [1,2,3]
b = a[:]


##TUPLA





##DICIONARIO