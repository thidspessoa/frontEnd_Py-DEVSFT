#Dicionário com 3 chaves e 3 valores;
agenda = {123: "Freeza", 733: "Kuririn", 874: "Goku"}


# Função com um parametro que verifique chave do dicionario.
#a função abaixo não tem "self" pois não esta dentro de uma classe
def verificarValor (chave):
    if chave in agenda:
        print("\nValor da chave: ")
        return agenda[chave]
        #if
    else:
        print("\nO valor inserido não corresponde a uma chave existente.\n")
    
consulta = int(input("Digite a chave a ser verificada: \n"))
print(verificarValor(consulta))




#Lista de contatos
contatos = {"Diana": 83890912, "Hugo":45679821, "Paulo":52781290, "Agua":98471092,
            "Markone":34317809, "Juçara":23419058}


def procurarContato (nome):
    if nome in contatos:
        print("O telefone é: ", contatos[nome])
    else:
        print("Este contato não existe na sua agenda.")

n = str(input("Digite o nome do contato: ")) 
procurarContato(n)
    