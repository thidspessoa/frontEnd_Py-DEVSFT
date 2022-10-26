# ENTRADAS
nomeHotel = input("Digite o nome do Hotel (até 6 caracteres):\n")

qntEstrelas = int(input("Digite em quantas estrelas o Hotel é classificado (Entre 1 e 5):\n"))
exibirEstrelas = str(qntEstrelas) + " estrela(s)"

cidadeHotel = input("Digite a cidade em que fica o hotel (até 8 caracteres):\n")

# SAIDA
print("-"*20)
print("|" + f'{nomeHotel:*^18}' + "|")
print("|" + f'{exibirEstrelas:*^18}' + "|")
print("|" + f'{cidadeHotel:*^18}' + "|")
print("-"*20)





""""
print ('-' * 20)
for _ in range (20-2):
    print('|' + '*' + nome * (20-2) + '|')
print ('-' * 20)
"""