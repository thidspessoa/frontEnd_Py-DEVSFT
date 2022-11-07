"""
print("Bem vindo ao jogo! Ao final, você terá uma pontuação baseada nos seus acertos. Vamos a primeira pergunta:")

print("\nEm que ano foi lançado o primeiro filme de Star Wars no cinema? ")
resposta1 = input("Sua resposta: ")

print("\nQual o nome do mestre Jedi que é verde e pequeno?")
resposta2 = input("Sua resposta: ")

print("Qual o primeiro nome do protagonista da trilogia original de Star Wars?")
resposta3 = input("Sua resposta: ")

print("O nome do vilão que se veste de preto e tem uma voz metálica é Darth ...")
resposta4 = input("Sua resposta: ")

print( "Escreva a letra da opção que NÃO é o nome de um título de filme da saga Star Wars. \n A) Uma nova Esperança \n B) O Retorno do Jedi \n C) Os Jedis Contra Atacam ")
resposta5 = input("Sua resposta: ")

if (resposta1 == "1997"):
    print("Parabéns! Você é um(a) Nerd Raiz.")
"""    

#Atividade sobre orientação a objetos:

#as classes devem iniciar com letra maiuscula em python.
#metodo self serve para dizer que as informações e variaveis dentro da classe pertencem a ela;
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mensagem(self):
        print("Seja bem vindo!")
        
class PessoaFisica():
    def __init__(self, nome, idade, CPF):
        self.nome = nome
        self.idade = idade
        self.CPF = CPF

    def mensagem(self):
        print("Seja bem vindo!")

class PessoaJuridica():
    def __init__(self, nome, idade, CNPJ):
        self.nome = nome
        self.idade = idade
        self.CNPJ = CNPJ
        
    def mensagem(self):
        print("Seja bem vindo!")
        
        
pessoa1 = Pessoa("Jandira", 19) #variavel de referencia para chamar a classe.
print(pessoa1.nome)
print(pessoa1.idade)        
        