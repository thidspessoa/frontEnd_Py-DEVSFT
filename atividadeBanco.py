salário = float(input("Salário: R$ "))
emprestimo = float(input("Digite o valor do emprestimo: R$"))

validação = salário * 0.5
validação2 = salário * 0.75

if (emprestimo <= validação):
    print("Seu emprestimo foi aprovado e o saldo cairá em sua conta em até 1 hora.")
elif (emprestimo <= validação2):
    print("Seu emprestimo está em analise e logo entraremos em contato para dar o retorno!")
else:
    print("Não foi possivel aprovar seu emprestimo no momento.")