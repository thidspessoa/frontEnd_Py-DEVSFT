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
"""
É possivel utilizar classes sem construtores, mas os construtores são 
usados para campos oobrigatorios de serem preenchidos no seu site. No banco de dados
seria o comando not null do MYSQQL, so permitindo o envio das informações caso
seja colocado algum dado como parametro para os contrutores.
"""
#as classes devem iniciar com letra maiuscula em python.
#metodo self serve para dizer que as informações e variaveis dentro da classe pertencem a ela;
class Pessoa(): #mãe 
    def __init__(self, nome, idade):
        self.__nome = nome #"__" é um mutator, oculta a instância.
        self.__idade = idade
        
    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def set_idade(self, nova_idade):
        self.__idade = nova_idade
    
    def mensagem(self):
        print("Seja bem vindo!")
        
class PessoaFisica(Pessoa): #filha esta erdando a função mensagem da classe PESSOA.
    def __init__(self, nome, idade, CPF):
        super().__init__(nome, idade)
        self.CPF = CPF
        
    def calculoImposto(self, *salario): #função #transformar a o parametro salario em uma tupla, faz com que o usuario possa inserir mais de uma vez um valor nesta variavel.
        
        #for faz varredura em uma tupla;
        salarios = 0 #acumulador
        for e in salario:
            ir = e * 0.015
            print("Seu imposto de renda é R$: ", ir)
            salarios += ir
        return salarios

class PessoaJuridica(): #filha
    def __init__(self, nome, idade, CNPJ):
        self.nome = nome
        self.idade = idade
        self.CNPJ = CNPJ
        
    def mensagem(self):
        print("Seja bem vindo!")
    
    def calculoImposto(self, salario, porteEmpresa): #função
        if (porteEmpresa == "pequeno"):
            print(salario*0.10)
        elif(porteEmpresa == "medio" or porteEmpresa == "médio"):
            print(salario*0.15)
        elif(porteEmpresa == "grande"):
            print(salario*0.20) 
         
        #print(salario * 0.10)


n = str(input("Digite o nome: "))
c = str(input("Digite a idade: "))
#x = str(input("Digite o CPF: "))
#y = str(input("Digite o CNPJ: "))
#i = str(input("Digite o porte da empresa: "))



#INSTANCIAMENTO

pessoa1 = Pessoa(n, c) #variavel de referencia para chamar a classe.
#Instanciamos a classe dentro da variavel passando parametros.
print(pessoa1.get_nome())
print(pessoa1.set_idade(22))
print(pessoa1.get_idade())    




"""
pessoa1 = PessoaJuridica(n, c, y)
print(pessoa1.mensagem())
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.CNPJ)
print(pessoa1.calculoImposto(123993, i))
"""

"""
pessoa3 = PessoaFisica(n, c, x)
print(pessoa3.mensagem())
print(pessoa3.nome)
print(pessoa3.idade)
print(pessoa3.CPF)
print(pessoa3.calculoImposto(233, 4444, 1212))
"""    


"""
pessoa2 = PessoaFisica("Jose", 18, 897498734)
print(pessoa2.mensagem())
print(pessoa2.CPF)
print(pessoa2.idade)
print(pessoa2.nome)
"""    
    
    
    
    
    

#METODOS
"""
dir + o comando: mostra detalhes soobre o ocmando, metodos e etc.
Ex:
print(dir(lista))
"""
