#Corrigindo erro

try:
  v = list(range(4))
  #V É uma lista com valores que vão de 0 a 3
  print("comando1")
  print(v[4])
  print("comando2")
except IndexError as e:
  print("A lista só possui 3 valores, não 4.")
  
  
"""Tratamos erros com try que seria um "execute" a linha de codigo, e o except seria um "caso ocorra"
o erro que colocarmos lá, vinculamos a uma variavel e executamos um comando para que o sistema não
pare no erro(Algum tipo de instrução ao usuario.)"""

#Multiplos excepts

v1 = [4, 8, 16, 32, 64, 128]
v2 = [2, 0, 4, 8, 0]

#Vamos efetuar a divisão entre o v1 e v2
for i in range(len(v1)):
  try:
    div= v1[i]/v2[i]
    print("%d/%d = %d" %(v1[i], v2[i], div))
  except:
    print("ERROR")

  """except (ZeroDivisionError, IndexError):#familia
    print("Error")"""    

  """except ZeroDivisionError as e:
    print("Impossivel dividir por 0")
  except IndexError as e:
    print("tamanhos de listas diferentes")"""
